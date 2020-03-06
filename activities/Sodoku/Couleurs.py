_ROUGE = "\033[1;31;40m"
_VERT = "\033[1;32;40m"
_JAUNE = "\033[1;33;40m"
_BLEU = "\033[1;34;40m"
_BLANC = "\033[0;47;40m"
_BBLANC = "\033[1;47;40m"


def Rouge(text : str):
    if (type(text) is not str): text = str(text)
    return _ROUGE + text + _BLANC 
def Vert(text : str):
    if (type(text) is not str): text = str(text)
    return _VERT + text + _BLANC 
def Jaune(text : str):
    if (type(text) is not str): text = str(text)
    return _JAUNE + text + _BLANC
def Bleu(text : str):
    if (type(text) is not str): text = str(text)
    return _BLEU + text + _BLANC
def Blanc(text : str):
    if (type(text) is not str): text = str(text)
    return _BLANC + text + _BLANC
def BlancGras(text : str):
    if (type(text) is not str): text = str(text)
    return _BBLANC + text + _BLANC
