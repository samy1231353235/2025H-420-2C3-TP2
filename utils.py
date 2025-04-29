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

def sauvegarder_json(data, chemin):
    """
    Sauvegarder des données dans un fichier JSON.
    """
    with open(chemin, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def ecrire_texte(contenu, chemin):
    """
    Écrire du texte brut dans un fichier texte (.txt).
    """
    with open(chemin, mode='w', encoding='utf-8') as f:
        f.write(contenu)
