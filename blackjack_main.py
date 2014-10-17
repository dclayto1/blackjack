import blackjack
import Tkinter


def update(game):
	while game.getGameState() == True:
		game.update()


def test(game):
	game.startShoe(1)
	game.getDeck().displayDeck()
	game.showTable()
	game.deal()
	game.deal()
	game.showTable()


def main():

	top = Tkinter.Tk()
	top.mainloop()

	game = blackjack.Blackjack()
	test(game)
	


main()