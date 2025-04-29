# utils.py

import csv
import json

def lire_csv(chemin):
    """
    Lire un fichier CSV et retourner la liste des lignes.
    Chaque dictionnaire correspond à une ligne du fichier.
    """
    donnees = []
    with open(fichier, mode='r', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            donnees.append(ligne)
    return donnees
    

def sauvegarder_json(data, chemin):
    """
    Sauvegarder des données dans un fichier JSON.
    - data : un objet Python (par exemple, un dictionnaire ou une liste)
    - chemin : chemin du fichier JSON à écrire
    Utiliser json.dump avec indentation pour que le fichier soit lisible.
    """
    with open(fichier, mode='w', encoding='utf-8') as f:
        json.dump(objet, f, indent=4, ensure_ascii=False)
    

def ecrire_texte(contenu, chemin):
    """
    Écrire du texte brut dans un fichier texte (.txt).
    - contenu : texte à écrire
    - chemin : chemin du fichier texte à créer
    """
    with open(fichier, mode='w', encoding='utf-8') as f:
        f.write(texte)
