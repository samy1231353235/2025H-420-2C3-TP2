import csv
import json

def lire_csv(chemin):
    # lit un fichier csv et retourne les lignes (sauf l'en-tête)
    with open(chemin, mode='r', newline='', encoding='utf-8') as f:
        lecteur = csv.reader(f)
        next(lecteur)  # saute la première ligne
        return [ligne for ligne in lecteur]

def sauvegarder_json(objet, chemin):
    # sauvegarde un objet dans un fichier json
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(objet, f, ensure_ascii=False, indent=4)

def ecrire_texte(texte, chemin):
    # écrit du texte dans un fichier texte
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(texte)
