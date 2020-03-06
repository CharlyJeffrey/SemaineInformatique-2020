from Couleurs import *
from Grilles import *
import numpy as np


def ObtenirCasesVides(grid : list, isCaseEmpty : list):
    """Fonction pour obtenir la grille qui détermine si les cases sont initialement vide.
    
    Arguments:
        grid {array} -- Grille de jeu initiale
        isCaseEmpty {array} -- Grille qui détermine si une case est vide ou non
    
    Return:
        casesVide {int} -- Nombre de cases vides
    """

    emptyCases = 0

    # Boucle sur la grille
    for i in range(9):
        for j in range(9):
            # Détermine si l'élément (i, j) est vide
            if (grid[i][j] == 0):
                isCaseEmpty[i][j] = True
                emptyCases += 1
    # Retourne la grille
    return emptyCases
    

def AfficherGrille(grid : list, isCaseEmpty : list):
    """Fonction pour afficher la grille de jeu.
    
    Arguments:
        grid {list} -- Grille de jeu
        isCaseEmpty {list} -- Grille pour détermine si la case était initialement vide
    """
    # |   |   |   ||   |   |   ||   |   |   |
    ligne = "============="*3
    dash =  "-------------"*3

    print(ligne)
    # Boucle sur les rangé
    for i in range(9):
        row = "|"
        
        # Boucle sur les colonnes
        for j in range(9):
            # Si la case est libre et initialement vide
            if isCaseEmpty[i][j] and grid[i][j] == 0:
                row += "   |"
            # Si la case est initialement vide, mais pas libre
            elif isCaseEmpty[i][j]:
                row += " "+Vert(grid[i][j])+" |"
            # Sinon, chiffre initialement présent dans la grille
            else:
                row += " "+BlancGras(grid[i][j])+" |"
            # Ajoute une ligne si c'Est la fin d'une sous-grille
            if ((j+1)%3 == 0) and (j is not 8): row += "|"

        # Affiche la rangé
        print(row)

        # Affiche une double-ligne ou une ligne simple selon le cas
        if (i%3 == 2): print(ligne)
        else: print(dash)

def ObtenirChoixJoueur(grid : list, isCaseEmpty : list):
    """Fonction pour obtenir la case et le chiffre que le joueur veut jouer
    """
    while(True):
        # Demande le choix du joueur
        print("Entrez le numéro de la rangé suivi de la colonne et du chiffre que vous voulez placer.")
        # Obtient le choix et le sépare aux espacements
        choix = input().split()

        # Vérifie si le choix est valide
        if (len(choix) is not 3):
            print(Jaune("Votre choix doit contenir la rangé, la colonne puis le chiffre que vous voulez placer."))
        else:
            # Vérifie que les arguments entrés sont des nombres
            try: 

                # Vérifie que les arguments sont des chiffres
                choix = [int(choix[0]), int(choix[1]), int(choix[2])]

                # Contrainte sur la rangé
                if (choix[0] < 0 or 8 < choix[0]):
                    print(Jaune("Le premier argument doit être un chiffre entre 0 et 8"))
                
                # Contrainte sur la colonne
                elif (choix[1] < 0 or 8 < choix[1]):
                    print(Jaune("Le second argument doit être un chiffre entre 0 et 8"))

                # Contrainte sur le chiffre ajouté
                elif (choix[2] < 1 or 9 < choix[2]):
                    print(Jaune("Le dernier argument doit être un chiffre entre 1 et 9"))

                # Vérifie que la case peut être modifiée
                elif (isCaseEmpty[choix[0]][choix[1]] != True):
                    print(Jaune("La case ne peut pas être modifiée!"))
                
                # Choix valide
                else:
                    return choix
        
            # Arguments entrés ne sont pas convertibles en int
            except ValueError:
                print(Jaune("Vous devez entrer des chiffres entre 0 et 8 pour les deux premiers arguments"))
                print(Jaune("et un chiffre entre 1 et 9 pour le troisième."))


def ChiffreValide(choix : list, grid : list):
    """
    Fonction pour déterminer si le chiffre placé est bon.
    
    Arguments:
        choix {list} -- Choix du joueur (rangé, colonne, chiffre)
        grid {list} -- Grille de jeu
    
    Returns:
        bool -- Vrai si le chiffre est possiblement bon.
    """
    # Obtient la rangé, colonne et chiffre
    row = choix[0]
    col = choix[1]
    num = choix[2]

    # Obtient les indices de la sous-grille
    _row = (row // 3) * 3
    _col = (col // 3) * 3

    # Vérifie si le chiffre se trouve dans la même rangé
    for i in range(9):
        if (grid[row][i] == num and i is not col):
            print(Rouge("ERREUR! Chiffre déjà présent dans la rangé."))
            return False
    # Vérifie si le chiffre se trouve dans la même colonne
    for i in range(9):
        if (grid[i][col] == num and i is not row):
            print(Rouge("ERREUR! Chiffre déjà présent dans la colonne!."))
            return False
    # Vérifie si le chiffre se trouve dans la même sous-grille
    for i in range(_row, _row+3):
        for j in range(_col, _col+3):
            if (i != row and j != col and grid[i][j] == num):
                print(Rouge("ERREUR! Chiffre déjà présent dans la sous-grille!"))
                return False
    # Aucune faute détectée
    return True

def PlacerChiffre(choice : list, grid : list):
    """
    Fonction pour placer le choix du joueur dans la grille de jeu.
    
    Arguments:
        choice {list} -- Choix du joueur
        grid {list} -- Grille de jeu
    """
    grid[choix[0]][choix[1]] = choix[2]
    return



def ChiffrePossible(grid : list, row : int, col : int, num : int):
    """
    Fonction pour déterminer si un chiffre peut possiblement 
    être placé dans une case spécifique. 
    
    Arguments:
        grid {list} -- Grille de jeu
        row {int} -- Rangé
        col {int} -- Colonne
        num {int} -- Chiffre à vérifier
    
    Returns:
        bool -- Vrai si le chiffre peut être placer dans la case.
    """
    # Vérifie si le nombre est déjà présent dans la rangé
    for i in range(0, 9):
        if (grid[row][i] == num):
            return False
    # Vérifie si le nombre est déjà présent dans la colonne
    for i in range(0, 9):
        if (grid[i][col] == num):
            return False
    # Vérifie si le nombre est déjà présent dans la sous-grille
    _row = (row // 3) * 3
    _col = (col // 3) * 3
    for i in range(_row, _row+3):
        for j in range(_col, _col+3):
            if (grid[i][j] == num):
                return False
    # Le nombre peut se retrouve à l'emplacement (row, col)
    return True

    

def AfficherSolution(grid : list, isCaseEmpty : list):
    """
    Fonction pour afficher la solution d'une grille de jeu.
    
    Arguments:
        grid {list} -- Grille de jeu
        isCaseEmpty {list} -- Grille de jeu initiale
    """
    # Boucle sur la grille de jeu
    for i in range(9):
        for j in range(9):
            # Vérifie si la case est vide
            if (grid[i][j] == 0):
                # Essaie de placer tous les chiffres
                for n in range(1, 10):
                    # Vérfie si le nombre peut etre placer
                    if (ChiffrePossible(grid, i, j, n)):
                        # On place le chiffre
                        grid[i][j] = n
                        # Récursion
                        AfficherSolution(grid, isCaseEmpty)
                        # Si on bloque, on remplace le chiffre par 0
                        grid[i][j] = 0
                return

    AfficherGrille(grid, isCaseEmpty)


# Grille de jeu
grille = ChoisirGrilleAleatoire()

# Nombre de vide
VIES = 3

# Initialise une grille vide
grilleVide = np.zeros(shape = (9,9), dtype = bool)

# Initialise la grille solution
grilleSolution = grille.copy()

# Nombre de cases à remplir
caseVides = ObtenirCasesVides(grille, grilleVide)


# Boucle de jeu principale
while (VIES > 0 and caseVides > 0):
    # Affiche vies restantes
    print(Blanc("Vies restantes: ") + VIES*Bleu("# "))
    # Affiche la grille de jeu
    AfficherGrille(grille, grilleVide)
    # Obtient le choix du joueur
    choix = ObtenirChoixJoueur(grille, grilleVide)
    # Détermine si le choix est bon
    if (ChiffreValide(choix, grille)):
        # Détermine si la case était vide; 
        if (grille[choix[0]][choix[1]] == 0): caseVides -= 1
        # Place le chiffre
        PlacerChiffre(choix, grille)
    # Sinon; enlève une vie
    else: 
        print(Rouge("Vous avez perdu une vie!"))
        VIES -= 1

# Si le joueur a gagné
if (VIES > 0):
    # Affiche la grille
    AfficherGrille(grille, grilleVide)
    # Message de félicitation
    print(Vert("Bravo! Vous avez gagné!"))
# Sinon, le joueur a perdu
else:
    print(Jaune("Vous n'avez plus de vie :("))
    print(Jaune("Vous avez perdu la partie :("))
    print()
    print(Bleu("La solution était: "))
    AfficherSolution(grilleSolution, grilleVide)