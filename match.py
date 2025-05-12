class Match:
    def __init__(self, joueur1, joueur2):
        # crée un match avec 2 joueurs et des scores à 0
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = 0
        self.score2 = 0

    def definir_scores(self, score1, score2):
        # enregistre les scores du match
        self.score1 = score1
        self.score2 = score2

    def gagnant(self):
        # retourne le gagnant du match
        if self.score1 > self.score2:
            return self.joueur1
        elif self.score2 > self.score1:
            return self.joueur2
        else:
            return None  # égalité
