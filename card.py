class Card:

	def __init__(self, suit, value):
		self.__suit = suit
		self.__value = value

	def __str__(self):
		return "%s%s" % (self.__value[0], self.__suit)

	def __cmp__(self, other):
		if self.__value[1] < other.getValue()[1]:
			return -1
		elif self.__value[1] == other.getValue()[1]:
			return 0
		elif self.__value[1] > other.getValue()[1]:
			return 1

	def getSuit(self):
		return self.__suit

	def getValue(self):
		return self.__value