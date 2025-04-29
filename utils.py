import csv
import json

def lire_csv(chemin):
    """
    Lire un fichier CSV et retourner la liste des lignes.
    Chaque liste représente une ligne du fichier (sans l’en-tête).
    """
    with open(chemin, mode='r', newline='', encoding='utf-8') as f:
        lecteur = csv.reader(f)
        next(lecteur)  # Ignorer l'en-tête
        return [ligne for ligne in lecteur]