import deck
import card
import player


class Blackjack:

	def __init__(self):
		self.__rules = "S17" #(stick on 17) or H17 (hit on 17)
		self.__numPlayers = 1
		self.__players = [player.Player("PLAYER", "Player 1")]
		self.__deck = deck.Deck()
		self.__dealer = player.Player("DEALER", "Dealer")
		self.__turn = 1

	def __str__(self):
		return "Stick on 17, or Hit on 17 = %s\nNumber of players = %d\n%s" % (self.getRules(), self.getNumPlayers(), self.getDeck())

	def getTurn(self):
		return self.__turn

	def getTurnName(self):
		if self.__turn == 0:
			return self.getDealer().getName()
		else:
			return self.getPlayers()[self.__turn - 1].getName()

	def getRules(self):
		return self.__rules

	def setRules(self, rule):
		self.__rules = rule


	def getNumPlayers(self):
		return self.__numPlayers

	def setNumPlayers(self, num):
		if num < self.__numPlayers:
			self.__players = self.__players[0:num]
		elif num > self.__numPlayers:
			start = self.__numPlayers+1
			end = num+1
			for i in range(start,end):
				name = "Player "+str(i)
				self.__players.append(player.Player("PLAYER", name))
		self.__numPlayers = num

	def getPlayers(self):
		return self.__players

	def getDealer(self):
		return self.__dealer


	def getDeck(self):
		return self.__deck


	def getNumDecks(self):
		return self.__deck.getNumberOfDecks()

	def setNumDecks(self, num):
		self.__deck.setNumberOfDecks(num)
		self.startShoe(num)


	def startShoe(self, numDecks):
		self.__deck.setNumberOfDecks(numDecks)
		self.__deck.initDeck()
		for shuffleCount in range(8):
			self.__deck.shuffleDeck()


	def startHand(self):
		for each in self.__players:
			each.clearHand()
		self.getDealer().clearHand()

	def deal(self):
		self.startHand()
		for i in range(2):
			for player in self.__players:
				player.hit(self.getDeck())
			self.__dealer.hit(self.getDeck())

		self.__turn = 1
		print "Cards are dealt"


	def playerHit(self):
		if self.__turn == 0:
			if self.getDealer().getHandValue() < 17:
				self.getDealer().hit(self.getDeck())
				print self.getDealer().getName()+" hits"
			else:
				print "Dealer cannot hit on 17 or above"
		else:
			if self.getPlayers()[self.__turn - 1].getHandValue() < 21:
				self.getPlayers()[self.__turn - 1].hit(self.getDeck())
				print self.getPlayers()[self.__turn - 1].getName()+" hits"
			else:
				print "Player either hit 21 or busted"


	def playerStay(self):
		stayStr = ""
		if self.__turn == 0:
			stayStr = self.getDealer().getName()+" stays"
		else:
			stayStr = self.getPlayers()[self.__turn - 1].getName()+" stays"

		self.__turn += 1
		if self.__turn > self.getNumPlayers():
			self.__turn = 0
		print stayStr
		newTurn = self.getTurnName()+"'s turn!"
		print newTurn
		return newTurn



	def showTable(self):
		print "%s" % (self.__dealer.displayDealer())
		for eachPlayer in self.__players:
			print "%s" % (eachPlayer.displayHand())


	def update(self):
		print "update"
