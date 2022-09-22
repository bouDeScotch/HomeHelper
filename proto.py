def mainLoop():
	mode = "non"
	while mode not in (1, 2, "quit"):
		mode = input("Which mode use ? \n1 - Flash card \n2 - Agenda\n\n")
		try:
			mode = int(mode)
		except:
			continue

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

	def getCards():

		CARALIST = ["Question", "Réponse", "DateCreation",
					"DerniereRevision", "Par coeur"]

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

	def studying():
		print(getCards())

	def creation():
		pass

	action = "non"
	while action not in (1, 2, "quit"):
		action = input(
			"Do you want to : \n1 - Create new flash cards \n2 - Study the existing flash cards \n\n")
		try:
			action = int(action)
		except:
			continue

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
