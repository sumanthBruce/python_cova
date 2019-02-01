from BlackJackGame.Deck import Deck
from BlackJackGame.BetRaja import Betting

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


def startGame():
    print("Lets play Black Jack Game \n how much do you want to bet.")
    chipVal = chipBet()
    betValue = Betting()

    deck = Deck(suits,ranks)
    deck.shuffel()
    playerCards=[]
    dealerCards=[]

    playerCards.append(deck.deal())
    playerCards.append(deck.deal())

    dealerCards.append(deck.deal())
    dealerCards.append(deck.deal())

    show_PlayCards(playerCards,dealerCards)





def show_PlayCards(playerCards,dealerCards):
    print("Dealer Cards: \n", dealerCards[0].__str__() +"\n <Not revealed>")
    print("\nPlayers Cards: " ,*playerCards, sep='\n')



def chipBet():
    chips=0;

    while True:

        try:
            chips= int(input())
        except ValueError:
            print("Give some real value my friend")

        else:
            print(chips)
            if chips > 100:
                print("Bet cant exceed Bet")
            else:
                break

    return chips

startGame()
