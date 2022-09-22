def mainLoop():
    mode = "non"
    while mode not in (1, 2, "quit"):
        mode = input("Which mode use ? \n1 - Flash card \n2 - Agenda\n\n")
    
    if (mode == 1):
        flashCard()
    elif (mode == 2):
        agenda()
    
    if (mode != "quit"):
        mainLoop()
    else:
        quiting()

def quiting():
    print("Currently stopping the program")

def flashCard():

    def creation():
        pass

    def studying():
        pass

    
    action = "non"
    while action not in (1, 2, "quit"):
        action = input("Do you want to : \n1 - Create new flash cards \n2 - Study the existing flash cards")
    
    if (action == 1):
        creation()
    elif (action == 2):
        studying()
    
    if (action != "quit"):
        flashCard()

def agenda():
    print("Mode en cours de construction")

if (__name__ == "__main__"):
    mainLoop()