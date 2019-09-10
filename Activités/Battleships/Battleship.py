import os.path
import sys
from random import randint
from math import log2

class Battleship :
    """
        Constructeur de la classe.
        Initialise les valeurs possibles pour les rangées et les colonnes ainsi que la grille de jeu et le nombre de navires.
        
        Arguments:
            row {list} -- Liste des caracteres pour les rangées.
            col {list} -- Liste des caracteres pour les colonnes.
            nships {int} -- Nombre de navires averses qui seront générés.
     """

    __slots__ = ["_row_char", "_col_char", "_row", "_col", "_nships", "_nteam", "_grid", "_char"]

    def __init__(self, row_char : list, col_char : list, nships : int, nteam : int) :
        
        # Initialise les attributs
        self._row_char = row_char
        self._col_char = col_char
        self._row = []
        self._col = []
        self._nships = nships
        self._nteam = nteam
        self._char = col_char + row_char 

        # Initialise les valeurs des rangées
        for i in range(len(row_char) - 1):
            # ie caractere
            l = row_char[i]
            # Boucle sur les autres caracteres
            for j in range(len(row_char)):
                if (j == i): continue
                # Obtient le je caractere
                k = row_char[j]
                # Ajoute 'lk' a row
                self._row.append(l+k)
        # Initialise les valeurs des colonnes
        for i in range(len(col_char)):
            self._col.append(col_char[i])

        # Initialise une grille de jeu
        self._grid = [None] * len(self._row) * len(self._col)
        for i in range(len(self._row)):
            for j in range(len(self._col)):
                self._grid[i*len(self._col) + j] = self._row[i] + self._col[j]
            # FIN BOUCLE 'j'
        # FIN BOUCLE 'i'
        return

    @staticmethod
    def OpenFile(PATH : str, FILE_NAME : str):
        """
        Méthode pour ouvrir un fichier qui se trouve dans un répertoire.
        
        Arguments:
            PATH {str} -- Chemin du répertoire où le fichier est sauvegardé.
            FILE_NAME {str} -- Nom du fichier à ouvrir.
        """
        try:
            fp = open(PATH +"/"+ FILE_NAME, "w")
            return fp
        except FileNotFoundError:
            print("\033[0;31mERROR:\033[00m Directory or File not found:")
            print("~"+PATH+"/"+FILE+"\n")
            print("Exit program.")
            exit()
    
    @staticmethod
    def CreateDirectories(PATH = None):
        """
        Méthode pour générer les répertoires où seront enregistrés les fichiers
        
        Keyword Arguments:
            PATH {str} -- Chemin (default: {None})
        """
        # Si un chemin est précisé, le répertoire y est ajouté 
        if PATH:
            PATH += "/Battleships"
        # Sinon, ajoute le répertoire au répertoire présent
        else:
            PATH = os.getcwd() + "/Battleships"

        # Chemin où seront enregistrés les fichiers
        FILE_PATH_TEAM = PATH + "/Equipes"

        # Crée les répertoires
        try:
            os.mkdir(PATH)
            os.mkdir(FILE_PATH_TEAM)
            print(f"Directory created: \033[0;32m{FILE_PATH_TEAM}\033[00m")
        except FileExistsError:
            print("\033[0;33mWARNING:\033[00m Directories already exist:")
            print(f"~{FILE_PATH_TEAM}")
        
        return PATH, FILE_PATH_TEAM

    def GenerateCoord(self):
        """
        Méthode pour générer les coordonnées.
        
        Returns:
            coord {list} -- Coordonnées non encryptées
            enc {list} -- Coordonnées encryptées
        """
        # Initialise des listes vides
        coord = []
        encrypted = []
        # Liste des indices possibles
        _i = [i for i in range(len(self._grid))]
        # Obtient les coordonnées
        for _ in range(self._nships):
            # Choisi une coordonnée aléatoire
            index = _i.pop(randint(0, len(_i)-1))
            coord.append(str(index))
            # Obtient la version encryptée
            c = self._grid[index]
            _c = ""
            for i in range(len(c)):
                # Obtient le string binaire de la valeur 'ASCII' du char
                _c += bin(ord(c[i]))[2:]
                if (i + 1 != len(c)):
                    _c += '-'
            encrypted.append(_c)
        return coord, encrypted
    
    def GenerateFiles(self, PATH : str, PATH_TEAM : str):
        """
        Méthode pour générer les fichiers «config.json» et «Equipe_XX.txt».
        Le fichier «config.json» contient la configuration du jeu et
        les fichiers «Equipe_XX.txt» contiennent les coordonnées encryptées.
        
        Arguments:
            PATH {str} -- Chemin principale.
            PATH_TEAM {str} -- Chemin où les fichiers des coordonnées encryptées seront.
        """
        # Crée le fichier config.json
        config = Battleship.OpenFile(PATH, "config.json")
        config.write('var config = {\n')
        # Liste des caracteres
        config.write('    "char" : [')
        for i in range(len(self._char) - 1):
            config.write('"' +self._char[i]+ '", ')
        config.write('"' +self._char[i+1]+ '"],\n')
        # Nombre de bateaux
        config.write('    "nships" : ' + str(self._nships) + ',\n')
        # Nombre d'équipes
        config.write('    "nteam" : ' + str(self._nteam) + ',\n')
        # Grille de jeu
        config.write('    "shape" : [' +str(len(self._row))+ ", " +str(len(self._col))+ "],\n")
        config.write('    "grid" : [')
        for i in range(len(self._grid) - 1):
            config.write(str(i)+ ", " )
        config.write(str(i+1) +'],\n')

        coords = []
        # Crée les fichiers encryptés
        for i in range(1, self._nteam + 1) :
            coord, enc = self.GenerateCoord()
            coords.append(coord)
            self.WriteEncryptedFile(i, enc, PATH_TEAM)

        # Ajoute les solutions à config
        # Écrit les coordonnées
        config.write('    "coords" : [')
        for i in range(self._nteam - 1):
            if (i != 0) :config.write('                ')
            config.write('[')
            for j in range(self._nships - 1):
                config.write(str(coords[i][j]) + ', ')
            config.write(str(coords[i][j+1]) + '],\n')
        config.write('                [')
        for j in range(self._nships - 1):
            config.write(str(coords[i+1][j]) + ', ')
        config.write(str(coords[i][j+1]) + ']],\n')

        config.write("}")
        config.close()
    
    def WriteEncryptedFile(self, team : int, enc : list, PATH_TEAM : str):
        """
        Méthode pour générer le fichier qui contient les coodonnées encryptées.

        Arguments:
            team {int} -- Numéro de l'équipe
        """
        # Nom du fichier
        FILE_NAME = "Equipe_" +str(team)+ ".txt"
        
        # Ouvre les fichiers
        fp_e = Battleship.OpenFile(PATH_TEAM, FILE_NAME)

        # Boucle sur les coordonnées
        for i in range(len(enc) - 1):
            fp_e.write(enc[i] + " ")
        fp_e.write(enc[i])
        # Ferme le fichier
        fp_e.close()
         

if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) != 2:
        print("\033[0;33mWARNING:\033[00m Invalid arguments.")
        print("         Usage: python3 Battleship.py number_of_ships number_of_team")
        print("         The default parameters will be use.\n")
        nships = 17
        nteam = 15
    else:
        try:
            nships = int(args[0])
            nteam = int(args[1])
        except ValueError:
            print("\033[0;31mERROR:\033[00m The parameters need to be integers.")
            print("       The default parameters will be use.\n")
            nships = 17
            nteam = 15

    row = ["A", "B", "C", "D"]
    col = [str(i) for i in range(10)]

    Generator = Battleship(row, col, nships, nteam)
    PATH, PATH_EQUIPE = Battleship.CreateDirectories()
    Generator.GenerateFiles(PATH, PATH_EQUIPE)