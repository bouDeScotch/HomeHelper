def mainLoop():
    mode = "non"
    while type(mode) != int and mode not in (1, 2, "quit"):
        mode = input("Which mode use ? \n1 - Flash card \n2 - Agenda\n\n")
        try:
            mode = int(mode)
        except:
            if mode == "quit":
                break
    
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
    print("Mode en cours de construction")

def agenda():
    print("Mode en cours de construction")

if (__name__ == "__main__"):
    mainLoop()