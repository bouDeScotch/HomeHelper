def create():
    pass

def action():
    pass

def getCards():

    CARALIST = ["Question", "Réponse", "DateCreation",
                "DerniereRevision", "Par coeur", "Set"]

    allCards = []
    with open("cards.cd", 'r') as cards:
        cardsLines = cards.readlines()
    # Clean the \n
    for i, line in enumerate(cardsLines):
        cardsLines[i] = "".join(line.split("\n"))

    for card in cardsLines:
        cara = card.split(";")
        card = {}
        for idx, carac in enumerate(CARALIST):
            card[carac] = cara[idx]
        allCards.append(card)

    return allCards

def main():
    action = None
    while action not in (1, 2, "quit"):
        action = input(
            "Do you want to \n1 - Create new flash cards \n2 - Study the existing flash cards \n\n")
        try:
            action=int(action)
        except:
            continue
    
    if (action == 1):
        create()
    elif (action == 2):
        study()
    
    if (action!="quit"):
        main()