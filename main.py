# Ce fichier represente l'accueil, comme l'index.html sur un site

import fonctions.flashCard as flashCard
import fonctions.agenda as agenda
import time

def inputInAList(listeInputs: list[str], texte: str) -> str:
    """Une fonction qui permet de récuperer un input dans une liste de valeurs données

    Args:
            listeInputs (list[str]): la liste des inputs possibles
            texte (str): Le texte a affiché avant l'input de l'utilisateur

    Returns:
            str: l'input de l'utilisateur
    """
    inpt = None
    while inpt not in listeInputs:
        inpt = input(texte)
    return inpt

def quiting():
	"""La fonction appellée lorsque l'on quitte le logiciel, sera utile plus tard pour être sûr que tout est sauvegardé avant que l'on parte.
	"""
	print("Le logiciel est en train de quitter...")
	time.sleep(3)

def mainLoop():
    mode = inputInAList(
        ["1", "2", "quit"], "Quel fonction utilisé ? \n1 - Flash Card \n2 - Agenda\n\n")
    
    if (mode == "1"):
        flashCard.main()
    
    elif (mode == "2"):
        agenda.main()
    
    if (mode != "quit"):
        mainLoop()
    else:
        quiting()

try:
    mainLoop()
except KeyboardInterrupt:
    quiting()