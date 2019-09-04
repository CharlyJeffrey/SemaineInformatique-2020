# Liste des caractères possibles
CHAR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D']


# Fonction pour déchiffrer un string binaire
def dechiffreurBinaire(bstring : str):
    """
    Fonction pour déchiffrer une string binaire.

    Arguments:
        bstring {str} -- String bianire à déchiffrer
    """

    # Initialise la puissance
    p = len(bstring) - 1
    # Initialise le résultat
    n = 0
    # Boucle pour déterminer la valeur
    for b in bstring:
        if (b == '1'):
            n += 2 ** p
        p -= 1
    # Retourne la valeur
    return n

# Ouvre le fichier contenant les coordonnées
fp = open("Battleships/Equipes/Equipe_1.txt", "r")
# Lit le fichier
coords = fp.read()

# Split les coordonnées
coords = coords.split()

# Boucle sur chaque coordonnées
for coord in coords:
    # Variable pour la coordonnée déchiffrée
    coord_dechiffre = ""
    # Split les composantes
    splited_coord = coord.split("-")
    # Déchiffre le tout
    for c in splited_coord:
        coord_dechiffre += CHAR[dechiffreurBinaire(c)]
    # Affiche la coordonnée déchiffrée
    print(coord_dechiffre)
    