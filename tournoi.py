from joueur import Joueur
from match import Match
import utils

class Tournoi:
    def __init__(self, nom):
        # crée le tournoi avec un nom
        self.nom = nom
        self.joueurs = []  # liste vide de joueurs
        self.matchs = []   # liste vide de matchs

    def charger_joueurs(self, chemin_csv):
        # charge les joueurs depuis un fichier csv
        lignes = utils.lire_csv(chemin_csv)
        for ligne in lignes:
            pseudo = ligne[0]
            joueur = Joueur(pseudo)
            self.joueurs.append(joueur)
        print(str(len(self.joueurs)) + " joueurs chargés.")

    def charger_matchs(self, chemin_csv):
        # charge les matchs depuis un fichier csv
        lignes = utils.lire_csv(chemin_csv)
        for ligne in lignes:
            pseudo1 = ligne[0]
            pseudo2 = ligne[1]

            joueur1 = None
            joueur2 = None

            # cherche les bons joueurs
            for j in self.joueurs:
                if j.pseudo == pseudo1:
                    joueur1 = j
                if j.pseudo == pseudo2:
                    joueur2 = j

            # si on trouve les 2 joueurs, on ajoute le match
            if joueur1 is not None and joueur2 is not None:
                match = Match(pseudo1, pseudo2)
                self.matchs.append(match)

        print(str(len(self.matchs)) + " matchs chargés.")

    def saisir_scores(self):
        # l'utilisateur entre les scores
        for match in self.matchs:
            print("match: " + match.joueur1 + " vs " + match.joueur2)
            try:
                score1 = int(input("score de " + match.joueur1 + ": "))
                score2 = int(input("score de " + match.joueur2 + ": "))
                match.definir_scores(score1, score2)

                # ajoute 1 victoire au gagnant
                if score1 > score2:
                    for j in self.joueurs:
                        if j.pseudo == match.joueur1:
                            j.enregistrer_victoire()
                elif score2 > score1:
                    for j in self.joueurs:
                        if j.pseudo == match.joueur2:
                            j.enregistrer_victoire()
            except ValueError:
                print("erreur : entrez un nombre.")

    def afficher_classement(self):
        # affiche le classement selon les victoires
        joueurs_tries = sorted(self.joueurs, key=lambda j: j.victoires, reverse=True)
        print("classement des joueurs :")
        for joueur in joueurs_tries:
            print(joueur.pseudo + " - victoires : " + str(joueur.victoires))

    def sauvegarder(self, chemin_json):
        # sauvegarde le tournoi dans un fichier json
        joueurs_json = []
        for joueur in self.joueurs:
            joueurs_json.append(joueur.to_dict())

        donnees = {
            "nom": self.nom,
            "joueurs": joueurs_json
        }

        utils.sauvegarder_json(donnees, chemin_json)
        print("tournoi sauvegardé dans " + chemin_json)

    def generer_rapport(self, chemin_texte):
        # écrit un fichier texte avec les résultats
        contenu = "rapport du tournoi : " + self.nom + "\n\n"
        contenu += "résultats des matchs\n"

        for match in self.matchs:
            if match.score1 is not None and match.score2 is not None:
                contenu += match.joueur1 + " " + str(match.score1)
                contenu += " - " + str(match.score2) + " " + match.joueur2 + "\n"
            else:
                contenu += match.joueur1 + " vs " + match.joueur2 + " (non joué)\n"

        contenu += "\nclassement final\n"
        joueurs_tries = sorted(self.joueurs, key=lambda j: j.victoires, reverse=True)
        for joueur in joueurs_tries:
            contenu += joueur.pseudo + " - " + str(joueur.victoires) + " victoire(s)\n"

        utils.ecrire_texte(contenu, chemin_texte)
        print("rapport généré dans " + chemin_texte)
