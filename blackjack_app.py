from Tkinter import *
from card_paths import *
import blackjack
import player


def optionWindow(gameWindow,game):
	option = Toplevel(gameWindow)
	option.title("Options")
	width = 300
	height = 200
	option.minsize(width, height)
	option.resizable(width=False, height=False)
	option.grab_set()
	geom = "+%d+%d" % (gameWindow.winfo_rootx()+(gameWindow.winfo_width()/2)-(width/2), gameWindow.winfo_rooty()+(gameWindow.winfo_height()/2)-(height/1.25))
	option.geometry(geom)


	def applyCommand(rule, numPlayers, numDecks):
		game.setRules(rule)
		game.setNumPlayers(numPlayers)
		game.setNumDecks(numDecks)
		print "Changes Applied!\nRules: %s\nNumber of Players: %d\nNumber of Decks: %d" % (game.getRules(), game.getNumPlayers(), game.getNumDecks())
		option.destroy()
	def cancelCommand():
		print "Changes Canceled!\nRules: %s\nNumber of Players: %d\nNumber of Decks: %d" % (game.getRules(), game.getNumPlayers(), game.getNumDecks())
		option.destroy()

	rules = game.getRules()
	Newrules = StringVar()
	numPlayers = game.getNumPlayers()
	NewnumPlayers = IntVar()
	numDecks = game.getNumDecks()
	NewnumDecks = IntVar()

	# "Rule set:" | S17 | H17
	ruleFrame = Frame(option)
	ruleFrame.pack()
	ruleLabel = Label(ruleFrame, text="Rule Set: ")
	s17Radio = Radiobutton(ruleFrame, text="S17", variable=Newrules, value="S17")
	h17Radio = Radiobutton(ruleFrame, text="H17", variable=Newrules, value="H17")
	if rules == "S17":
		s17Radio.select()
	elif rules == "H17":
		h17Radio.select()
	ruleLabel.pack(side=LEFT)
	s17Radio.pack(side=LEFT)
	h17Radio.pack(side=LEFT)

	# "Number of Players" | scale
	numPlayersFrame = Frame(option)
	numPlayersFrame.pack()
	numPlayersLabel = Label(numPlayersFrame, text="Number of Players: ")
	numPlayersScale= Scale(numPlayersFrame, variable=NewnumPlayers, orient=HORIZONTAL, from_=1, to=3)
	numPlayersScale.set(numPlayers)
	numPlayersLabel.pack(side=LEFT)
	numPlayersScale.pack(side=LEFT)

	# "Number of Decks" | scale
	numDecksFrame = Frame(option)
	numDecksFrame.pack()
	numDecksLabel = Label(numDecksFrame, text="Number of Decks: ")
	numDecksScale= Scale(numDecksFrame, variable=NewnumDecks, orient=HORIZONTAL, from_=1, to=8)
	numDecksScale.set(numDecks)
	numDecksLabel.pack(side=LEFT)
	numDecksScale.pack(side=LEFT)

	# Apply | Cancel
	bottomFrame = Frame(option)
	bottomFrame.pack(side=BOTTOM)
	applyButton = Button(bottomFrame, text="Apply", command=lambda:applyCommand(Newrules.get(), NewnumPlayers.get(), NewnumDecks.get()))
	cancelButton = Button(bottomFrame, text="Cancel", command=cancelCommand)
	applyButton.pack(side=LEFT)
	cancelButton.pack(side=LEFT)


def initHandFrames():
	#DEALER FRAME
	dealerFrame = Frame(gameWindow, bd=5, relief=RIDGE, width=gameWindow.winfo_width())
	dealerFrame.pack()
	Label(dealerFrame, text=game.getDealer().displayDealer()).pack(side=TOP)
	for eachCard in game.getDealer().displayDealer().split()[2:]:
		name = "card_"+eachCard
		img = PhotoImage(file=paths[name])
		card = Label(dealerFrame, image=img)
		card.img = img
		card.pack(side=LEFT)


	#PLAYERS HANDS
	playersFrame = Frame(gameWindow, bg="dark green", width=gameWindow.winfo_width())
	playersFrame.pack(side=BOTTOM)
	playerFrames = []
	for person in game.getPlayers():
		playerFrame = Frame(playersFrame,bd=5, relief=RIDGE, width=gameWindow.winfo_width()/game.getNumPlayers())
		playerFrame.pack(side=RIGHT)
		Label(playerFrame, text=person.displayHand()).pack(side=TOP)

		for eachCard in person.displayHand().split()[3:]:
			name = "card_"+eachCard
			img = PhotoImage(file=paths[name])
			card = Label(playerFrame, image=img)
			card.img = img
			card.pack(side=LEFT)


def displayHands(game, gameWindow, playersFrame, playerList):
	for eachFrame in playerList:
		eachFrame.pack_forget()
		eachFrame.destroy()


	#DEALER FRAME
	dealerFrame = Frame(gameWindow, bd=5, relief=RIDGE, width=gameWindow.winfo_width())
	dealerFrame.pack()
	playerList.append(dealerFrame)
	Label(dealerFrame, text=game.getDealer().displayDealer()).pack(side=TOP)
	for eachCard in game.getDealer().displayDealer().split()[2:]:
		name = "card_"+eachCard
		img = PhotoImage(file=paths[name])
		card = Label(dealerFrame, image=img)
		card.img = img
		card.pack(side=LEFT)


	#PLAYERS HANDS
	for person in game.getPlayers():
		playerFrame = Frame(playersFrame,bd=5, relief=RIDGE, width=gameWindow.winfo_width()/game.getNumPlayers())
		playerFrame.pack(side=RIGHT)
		playerList.append(playerFrame)
		Label(playerFrame, text=person.displayHand()).pack(side=TOP)

		for eachCard in person.displayHand().split()[3:]:
			name = "card_"+eachCard
			img = PhotoImage(file=paths[name])
			card = Label(playerFrame, image=img)
			card.img = img
			card.pack(side=LEFT)



def gameScreen(game):
	gameWindow = Tk()
	gameWindow.title("Blackjack")
	gameWindow.minsize(640,480)
	gameWindow.maxsize(1600,900)
	gameWindow.resizable(width=True, height=True)
	gameWindow.configure(bg="dark green")

	def optionFunction():
		optionWindow(gameWindow, game)
		displayHands(game, gameWindow, playersFrame, playerList)
		
	def hitFunction():
		game.playerHit(game.getPlayers()[0])
		displayHands(game, gameWindow, playersFrame, playerList)


	#OPTION BUTTON
	optionButton = Button(gameWindow, text="Options", command=optionFunction)
	optionButton.pack(anchor=NW)


	#INITIALIZE FRAMES
	playersFrame = Frame(gameWindow, bg="dark green", width=gameWindow.winfo_width())
	playersFrame.pack(side=BOTTOM)
	playerList = []


	#PLAYER CHOICES
	hitButton = Button(gameWindow, text="player 1 hit", command=hitFunction)
	hitButton.pack()
	
	gameWindow.mainloop()






