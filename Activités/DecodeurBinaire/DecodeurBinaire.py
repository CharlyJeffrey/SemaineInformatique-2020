from math import log

# Première facon
def DecodeurBinaire(bstring : str):
    # Initialise le nombre
    n = 0
    # Taille de bstring
    length = len(bstring)
    # Boucle sur le nombre d'élément de bstring
    for i in range(length):
        # Détermine si le ie element s'agit de '1'
        if (bstring[i] == '1'):
            # Augmente la valeur de 'n'
            n += 2 ** (length - 1 - i)
    # Retourne la valeur de 'n'
    return n



# Première fonction 
def BinairyToDecimal(bstring : str):
    """
    Fonction pour passer de la représentation binaire à décimale

    Arguments:
        bstring {str} -- Nombre binaire
    
    Return:
        n {int} -- Nombre en base décimal résultant
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
    return str(n)
    

# De décimal à binaire
def DecimalToBinairy(dstring : str):
    """
    Fonction pour passer de la représentation décimale à binaire
    
    Arguments:
        dstring {str} -- Nombre décimal
    
    Returns:
        bstring {str} -- Nombre binaire
    """
    # Obtient la valeur numérique
    try:
        d = int(dstring)
    except ValueError:
        print("Le string '" +dstring+ "' n'est pas un nombre décimal.")
        return None

    # Initialise la puissance
    p = int(log(d) / log(2))

    # Initialise le résultat
    bstring = ""

    # Boucle pour déterminer le string binaire
    while (p >= 0):
        if (d - 2 ** p >= 0):
            bstring += '1'
            d -= 2 ** p
        else:
            bstring += '0'
        p -= 1
    
    # Retourne le résultat
    return bstring


def BaseOneToBaseTwo(b1_string: str, base_one: int, base_two: int):
    """
    Fonction pour passer de la représentation en base 1 vers la base 2
    
    Arguments:
        b1_string {str} -- Nombre représenté dans la base 1 (base_one)
        base_one {int} -- Base dans laquelle le nombre est représenté
        base_two {int} -- Base dans laquelle on veut représenter le nombre
    
    Returns:
        b2_string {str} -- Nombre représenté dans la base 2 (base_2)
    """
    # Obtient le nombre en base décimal
    d = 0
    for i in range(len(b1_string)):
        d += int(b1_string[i]) * base_one ** (len(b1_string) - i - 1)

    # Initialise la puissance
    p = int(log(d) / log(base_two))

    # Initialise le résultat
    b2_string = ""

    # Boucle pour déterminer le nombre dans la base 2
    while (p >= 0):
        # Compteur
        c = 0
        #
        while (d - base_two ** p >= 0):
            c += 1
            d -= base_two ** p
        # 
        b2_string += str(c)
        p -= 1
    
    return b2_string


