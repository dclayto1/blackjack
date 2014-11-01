import blackjack
import blackjack_app


def test(game):
	game.startShoe(1)
	game.setNumPlayers(3)
	game.getDeck().displayDeck()
	game.showTable()
	game.deal()	
	game.showTable()



def main():
	game = blackjack.Blackjack()
	test(game)
	blackjack_app.gameScreen(game)
	

main()