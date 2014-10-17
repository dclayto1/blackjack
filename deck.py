import random
import card

class Deck:
	def __init__(self):
		self.__cards = []
		self.__numDecks = 1
		self.__numCards = 52
		self.__currentCardIndex = -1

	def __str__(self):
		return "Number of decks = %d\nNumber of cards = %d" % (self.__numDecks, self.__numCards)


	def setNumberOfDecks(self, numDecks):
		self.__numDecks = numDecks
		self.__numCards = numDecks * 52


	def initDeck(self):
		__suits = ["C","D","H","S"]
		__values = [("2", 2),("3",3),("4",4),("5",5),("6",6),("7",7),("8",8),("9",9),("10",10),("J",10),("Q",10),("K",10),("A",11,1)]
		self.__cards = []
		for decks in range(1,self.__numDecks+1):

			for eachSuit in range(1,5):

				for eachValue in range(1,14):
					self.__cards.append(card.Card(__suits[eachSuit-1], __values[eachValue-1]))


	def getNumberOfDecks(self):
		return self.__numDecks


	def getNumberOfCards(self):
		return self.__numCards


	def getNextCard(self):
		self.__currentCardIndex += 1
		return self.__cards[self.__currentCardIndex]
			

	def displayDeck(self):
		__cardStr = ""
		for card in self.__cards:
			__cardStr += str(card) + " "
		print __cardStr


	def shuffleDeck(self):
		random.shuffle(self.__cards)