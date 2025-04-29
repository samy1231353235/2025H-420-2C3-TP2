from joueur import Joueur
from match import Match
import utils

class Tournoi:
    def __init__(self, nom):
        """
        Initialise un tournoi avec son nom.
        Initialise aussi une liste vide pour les joueurs et pour les matchs.
        """
        self.nom = nom
        self.joueurs = []
        self.matchs = []

    def charger_joueurs(self, chemin_csv):
        """
        Lire un fichier CSV contenant les joueurs.
        """
        lignes = utils.lire_csv(chemin_csv)
        for ligne in lignes:
            pseudo = ligne[0]
            self.joueurs.append(Joueur(pseudo))
        print(f"{len(self.joueurs)} joueurs chargés.")

    def charger_matchs(self, chemin_csv):
        """
        Lire un fichier CSV contenant les matchs.
        """
        lignes = utils.lire_csv(chemin_csv)
        for ligne in lignes:
            pseudo1, pseudo2 = ligne[0], ligne[1]
            joueur1 = next((j for j in self.joueurs if j.pseudo == pseudo1), None)
            joueur2 = next((j for j in self.joueurs if j.pseudo == pseudo2), None)
            if joueur1 and joueur2:
                self.matchs.append(Match(pseudo1, pseudo2))
        print(f"{len(self.matchs)} matchs chargés.")

    def saisir_scores(self):
        """
        Pour chaque match dans la liste des matchs :
        - Afficher le match
        - Demander à l'utilisateur d'entrer les scores
        - Déterminer le gagnant
        """
        for match in self.matchs:
            print(f"Match: {match.joueur1} vs {match.joueur2}")
            try:
                score1 = int(input(f"Entrez le score de {match.joueur1}: "))
                score2 = int(input(f"Entrez le score de {match.joueur2}: "))
                match.definir_scores(score1, score2)
                if score1 > score2:
                    gagnant = next((j for j in self.joueurs if j.pseudo == match.joueur1), None)
                    if gagnant:
                        gagnant.enregistrer_victoire()
                elif score2 > score1:
                    gagnant = next((j for j in self.joueurs if j.pseudo == match.joueur2), None)
                    if gagnant:
                        gagnant.enregistrer_victoire()
            except ValueError:
                print("Erreur : Veuillez entrer des scores valides.")

    def afficher_classement(self):
        """
        Afficher le classement des joueurs.
        """
        self.joueurs.sort(key=lambda j: j.victoires, reverse=True)
        print("Classement des joueurs :")
        for joueur in self.joueurs:
            print(f"{joueur.pseudo} - Victoires : {joueur.victoires}")

    def sauvegarder(self, chemin_json):
        """
        Sauvegarder le tournoi dans un fichier JSON.
        """
        donnees = {
            "nom": self.nom,
            "joueurs": [joueur.to_dict() for joueur in self.joueurs]
        }
        utils.sauvegarder_json(donnees, chemin_json)
        print(f"Tournoi sauvegardé dans {chemin_json}")

    def generer_rapport(self, chemin_texte):
        """
        Générer un rapport du tournoi sous forme de fichier texte.
        """
        contenu = f"Rapport du tournoi : {self.nom}\n\n"
        contenu += "=== Résultats des matchs ===\n"
        for match in self.matchs:
            if match.score1 is not None and match.score2 is not None:
                contenu += f"{match.joueur1} {match.score1} - {match.score2} {match.joueur2}\n"
            else:
                contenu += f"{match.joueur1} vs {match.joueur2} (non joué)\n"

        contenu += "\n=== Classement final ===\n"
        classement = sorted(self.joueurs, key=lambda j: j.victoires, reverse=True)
        for joueur in classement:
            contenu += f"{joueur.pseudo} - {joueur.victoires} victoire(s)\n"

        utils.ecrire_texte(contenu, chemin_texte)
        print(f"Rapport généré dans {chemin_texte}")
