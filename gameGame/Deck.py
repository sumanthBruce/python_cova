from BlackJackGame.GameCardValue import Card
import random
class Deck:
    def __init__(self,suits,ranks):
        self.deck =[];
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffel(self):
        random.shuffle(self.deck)

    def __str__(self):
        cardStament=""
        for card in self.deck:
            cardStament += card.__str__() +'\n'
        return cardStament

    def deal(self):
        singleCard = self.deck.pop();
        return singleCard;


