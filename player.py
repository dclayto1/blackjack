import card
import deck

class Player:

	def __init__(self, playerType, playerName):
		self.__hand = []
		self.__total = 0
		self.__playerType = playerType
		self.__playerName = playerName

	def hit(self, deck):
		self.__hand.append(deck.getNextCard())

	def stay(self):
		print 'stay'

	def split(self):
		print 'split'

	def doubleDown(self):
		print 'double down'

	def surrender(self):
		print 'surrender'

	def clearHand(self):
		self.__hand = []
		self.__total = 0

	def getHandValue(self):
		handCopy = self.__hand
		handCopy.sort()
		for each in handCopy:
			if ((each.getValue()[0] == "A") and ((self.__total+each.getValue()[1]) > 21)):
				self.__total += each.getValue()[2]
			else:
				self.__total += each.getValue()[1]

		return self.__total


	def displayDealer(self):
		if(self.__playerType == "DEALER"):
			if len(self.__hand) == 1:
				return "%s's hand: ??" % (self.__playerName)
			elif len(self.__hand) == 2:
				return "%s's hand: ?? %s" % (self.__playerName, self.__hand[1])
			else:
				return self.displayHand()
		else:
			return self.displayHand()

	def displayHand(self):
		cardStr = ""
		for each in self.__hand:
			cardStr += str(each) + " "
		#cardStr += "\n"

		return "%s's hand: %s" % (self.__playerName, cardStr)