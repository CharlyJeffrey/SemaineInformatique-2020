"""
    Introduction aux notions de base du langage Python.

    Notions abordées:
        * Variables (et types)
        * Opérations
        * Intéraction console
        * Fonction
"""

# Date actuelle
DATE_ANNEE = 2020
DATE_MOIS = 6
DATE_JOUR = 1

# Mapping des mois
MOIS = {
    "janvier"   : 1,
    "fevrier"   : 2,
    "mars"      : 3,
    "avril"     : 4,
    "mai"       : 5,
    "juin"      : 6,
    "juillet"   : 7,
    "aout"      : 8,
    "septembre" : 9,
    "octobre"   : 10,
    "novembre"  : 11,
    "decembre"  : 12
}

# Fonction pour obtenir l'age d'une personne
def ObtenirAge():
    # Demande l'année de naissance
    annee = input("Quelle est votre année de naissance? ")
    # Converti 'int'
    annee = int(annee)

    # Demande le moi de naissance
    mois = input("Quel est votre mois de naissance? ")
    # Converti en minuscule
    mois = mois.lower()
    # Obtient la valeur du mois
    mois = MOIS[mois]

    # Demande le jour de naissance
    jour = input("Quel est votre jour de naissance? ")
    # Converti en 'int'
    jour = int(jour)

    # Premiere evaluation de l'age
    age = DATE_ANNEE - annee

    # Correction sur le mois
    if (mois > DATE_MOIS) :
        age -= 1
    if (mois == DATE_MOIS and jour > DATE_JOUR) :
        age -= 1
    # En une seule condition ((mois == DATE_MOIS and jour > DATE_JOUR) or mois > DATE_MOIS)
    
    # Retourne l'age
    return age

def main():
    """
    Ce que les jeunes ecriveront dans leur fichier.
    """

    # Demande le nom de la personne
    nom = input("Quel est votre nom? ")

    # Obtient l'âge de la personne
    age = ObtenirAge()

    # Affiche le nom et l'age de la personne
    print()
    print(f"Bonjour {nom}! Vous avez {age} ans!")
    #print("Bonjour " + nom + "! Vous avez " + str(age) + " ans!")
    
    # Détermine si la personne est majeure
    if (age > 18) :
        print(f"Et vous êtes un adulte depuis au moins un {age-18} ans!")
    elif (age == 18) :
        print("Et vous venez d'avoir 18 ans!")
    else:
        print(f"Et vous allez avoir 18 ans d'ici {18-age} ans!")
    print()

    # Exemples boucle
    print("Votre nom contient les lettres suivantes: ")
    for lettre in nom : 
        print(lettre)
    print()

    # Exemple array
    table = []  # Liste vide
    n = 100     # Nombre d'éléments
    # Boucle pour remplir la lsite<
    for i in range(n):
        table.append(i)
    print(table)

    # Meme résultat; une ligne; plus efficace
    table = [i for i in range(n)]

    # Liste 2D
    table = []
    n = 10
    m = 5
    for i in range(n):
        table.append([i*m + j for j in range(m)])
        print(table[i])
    # FIN
    return

    


    
main()