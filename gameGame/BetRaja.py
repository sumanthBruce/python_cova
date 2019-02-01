

class Betting:

    def __int__(self,bet):
        self.total=100;
        self.bet=bet;
        self.didWin=True;

    def winningBet(self,bet):
        self.total +=self.bet
        self.didWin=True

    def lossingBet(self):
        self.total-=self.bet
        self.didWin=False;

    def __str__(self):
        if self.didWin:
            return "Player won the Match his pocket value is " +self.total
        else:
            return "Player lost the match his pocket value is " +self.total
