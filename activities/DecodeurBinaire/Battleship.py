from DecodeurBinaire import *

# Nom de leur fichier -change selon l'équipe-
NOM_FICHIER = "Equipe_1.txt"

def DecodeurCoordonnees(FILE_NAME : str):
    """
        Fonction pour obtenir les coordonnées des bateaux à partir
        d'un fichier contenant les coordonnées 'encryptées' en binaire.

        Arguments:
            FILE_NAME {str} -- Nom du fichier contenant les coordonnées.

    """
    # Ouvre le fichier
    f = open(FILE_NAME, 'r')
    # Obtient le contenu du fichier
    lines = f.readlines()
    # Boucle sur chacune des lignes
    for line in lines:
        # Affiche la ligne
        print(line)
        # Variable pour stocker la coordonnée
        coord = ""
        # Ignore le caractere '\n'
        enc_coord = line.replace('\n', '')
        # Sépare la ligne à chaque '-' rencontré
        enc_coord = enc_coord.split('-')
        # Boucle sur chaque élément
        for bstring in enc_coord:
            # Utilise la fonction 'BinairyToDecimal'
            n = BinairyToDecimal(bstring)
            # Obtient le caractère ASCII associé à 'n'
            c = str(chr(n))
            # Ajoute le caractere
            coord += c
        # Affiche la coordonnée décryptée
        print(coord)

# Utilise la fonction pour obtenir les coordonnées
DecodeurCoordonnees(NOM_FICHIER)

print("\n----------------------------------------------\n")

# Test de la fonction pour changement de base

rep_base_1 = "101"

base_1 = 10
base_2 = 2

print(BaseOneToBaseTwo(rep_base_1, base_1, base_2))