import csv
import json

def lire_csv(chemin):
    """
    Lire un fichier CSV et retourner la liste des lignes.
    Chaque liste représente une ligne du fichier (sans l’en-tête).
    """
<<<<<<< HEAD
    with open(chemin, mode='r', newline='', encoding='utf-8') as f:
        lecteur = csv.reader(f)
        next(lecteur)  # Ignorer l'en-tête
        return [ligne for ligne in lecteur]
=======
    donnees = []
    with open(fichier, mode='r', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            donnees.append(ligne)
    return donnees
    
>>>>>>> e9f21888660506f2a18d06ecb44b4553c63cbd10

def sauvegarder_json(data, chemin):
    """
    Sauvegarder des données dans un fichier JSON.
    """
<<<<<<< HEAD
    with open(chemin, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
=======
    with open(fichier, mode='w', encoding='utf-8') as f:
        json.dump(objet, f, indent=4, ensure_ascii=False)
    
>>>>>>> e9f21888660506f2a18d06ecb44b4553c63cbd10

def ecrire_texte(contenu, chemin):
    """
    Écrire du texte brut dans un fichier texte (.txt).
    """
<<<<<<< HEAD
    with open(chemin, mode='w', encoding='utf-8') as f:
        f.write(contenu)
=======
    with open(fichier, mode='w', encoding='utf-8') as f:
        f.write(texte)
>>>>>>> e9f21888660506f2a18d06ecb44b4553c63cbd10
