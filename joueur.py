class Joueur:
    def __init__(self, pseudo):
        # crée un joueur avec un pseudo et 0 victoire
        self.pseudo = pseudo
        self.victoires = 0

    def enregistrer_victoire(self):
        # ajoute 1 victoire
        self.victoires += 1

    def to_dict(self):
        # retourne les infos du joueur en dictionnaire
        return {
            "pseudo": self.pseudo,
            "victoires": self.victoires
        }

    @staticmethod
    def from_dict(data):
        # crée un joueur à partir d'un dictionnaire
        joueur = Joueur(data["pseudo"])
        joueur.victoires = data.get("victoires", 0)
        return joueur
