import deck
import card
import player


class Blackjack:

	def __init__(self):
		self.__gameState = "MENU"
		self.__rules = "S17" #(stick on 17) or H17 (hit on 17)
		self.__numPlayers = 1
		self.__players = [player.Player("PLAYER", "Player 1")]
		self.__deck = deck.Deck()
		self.__dealer = player.Player("DEALER", "Dealer")

	def __str__(self):
		return "Game state = %s\nStick on 17, or Hit on 17 = %s\nNumber of players = %d\n%s" % (self.getGameState(), self.getRules(), self.getNumPlayers(), self.getDeck())


	def getGameState(self):
		return self.__gameState


	def getRules(self):
		return self.__rules


	def getNumPlayers(self):
		return self.__numPlayers


	def getDeck(self):
		return self.__deck


	def startShoe(self, numDecks):
		self.__deck.setNumberOfDecks(numDecks)
		self.__deck.initDeck()
		for shuffleCount in range(8):
			self.__deck.shuffleDeck()


	def startHand(self):
		for each in self.__players:
			each.clearHand()

	def deal(self):
		for player in self.__players:
			player.hit(self.getDeck())
		self.__dealer.hit(self.getDeck())



	def showTable(self):
		print "%s" % (self.__dealer.displayDealer())
		for eachPlayer in self.__players:
			print "%s" % (eachPlayer.displayHand())


	def update(self):
		print "update"


'''def main():
	deck1 = deck.Deck()
	deck1.initDeck()
	deck1.displayDeck()
	





main()'''