from random import shuffle

class Card():
    suits = ["spades","hearts","diamonds","clubs"]

    values = [None,None,"2","3","4","5","6","7","8","9","10",
              "Jack","Queen","King","Ace"]

    def __init__(self,v,s):
        
       self.value = v
       self.suit = s
    def __opp__(self,c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False
        
    def __repr__(self):
        return self.values[self.value]+" of "+ self.suits[self.suit]

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
        
class player:
    def __init__(self,name):
        self.win = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("player1 name:")
        name2 = input("plyer2 name:")
        self.deck = Deck()
        self.p1 = player(name1)
        self.p2 = player(name2)

    def wins(self,winner):
        w = "{} win this round"
        w = w.format(winner)
        print(w)
        
    def draw(self,p1n,p1c,p2n,p2c):
        d = "{} draw {},{} draw {}"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)

    def play_games(self):
        cards = self.deck.cards
        print("beginning games")
        
        while len(cards)>=2:
            m = input("enter q to quite.enter other key to begin")
            if m == "q":
                break
            p1n = self.p1.name
            p2n = self.p2.name
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            self.draw(p1n,p1c,p2n,p2c)

            if p1c < p2c:
                self.p2.win += 1
                self.wins(p1n)
            else:
                self.p1.win +=1
                self.wins(p2n)
        win = self.winner(self.p1,self.p2)
        print("Game is over.{} wins".format(win))

    def winner(self,p1,p2):
        if p1.win > p2.win:
            return p1.name
        elif p1.win < p2.win:
            return p2.name
        return "It was a tie!"
            
        
G1=Game()
G1.play_games()
