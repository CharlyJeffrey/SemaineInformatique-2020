from math import log
 
def BinairyToDecimal(bstring : str):
    """
    Fonction pour passer de la représentation binaire à décimale

    Arguments:
        bstring {str} -- Representation binaire
    
    Return:
        n {int} -- Valeur décimal
    """
    # Vérifie que 'bstring' est un string
    if type(bstring) != str:
        print("L'argument doit être un string binaire")
        return
    # Vérifie si 'bstring' est bien une representation binaire
    for bit in bstring:
        if bit != '0' or bit != '1':
            print("L'argument n'est pas une representation binaire.")
            return
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
    

def DecimalToBinairy(dstring : str):
    """
    Fonction pour passer de la représentation décimale à binaire
    
    Arguments:
        dstring {str} -- Valeur décimal
    
    Returns:
        bstring {str} -- Representation binaire
    """
    # Obtient la valeur numérique
    try:
        d = int(dstring)
    except ValueError:
        print("Le string '" +dstring+ "' n'est pas un nombre entier.")
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


def BaseOneToBaseTwo(rep_base_one: str, base_one: int, base_two: int):
    """
    Fonction pour passer de la représentation en base 1 vers la base 2
    
    Arguments:
        rep_base_one {str} -- Nombre représenté dans la base 1 (base_one)
        base_one {int} -- Base dans laquelle le nombre est représenté
        base_two {int} -- Base dans laquelle on veut représenter le nombre
    
    Returns:
        rep_base_two {str} -- Nombre représenté dans la base 2 (base_2)
    """
    # Vérifie que les bases soient des chiffres
    if (type(base_one) != int or type(base_two) != int):
        try:
            base_one = int(base_one) 
            base_two = int(base_two)
        except ValueError:
            print("Les bases doivent être des chiffres en 1 et 10 inclusivement.")
            return

    # Vérifie que les bases soient entre 1 et 9 (inclusivement)
    if (base_one < 1 or 10 < base_one or base_two < 1 or 10 < base_two):
        print("Les bases doivent être des chiffres en 1 et 10 inclusivement.")
        return 
    
    # Obtient le nombre en base décimal
    d = 0
    for i in range(len(rep_base_one)):
        d += int(rep_base_one[i]) * base_one ** (len(rep_base_one) - i - 1)

    # Initialise la puissance
    p = int(log(d) / log(base_two))

    # Initialise le résultat
    rep_base_two = ""

    # Boucle pour déterminer le nombre dans la base 2
    while (p >= 0):
        # Compteur
        c = 0
        #
        while (d - base_two ** p >= 0):
            c += 1
            d -= base_two ** p
        # Ajoute le 'b2-bit'
        rep_base_two += str(c)
        p -= 1
    
    return rep_base_two