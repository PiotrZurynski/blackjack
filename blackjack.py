import random
class BlackJack:
    listakart=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    handValue=0
    def __init__(self):
        pass
    def hand(self):
        self.dealhand = random.sample(self.listakart, 2)
        if self.dealhand[0]=="J" or "Q" or "K" and self.dealhand[1] =="J" or "Q" or "K":
            self.handValue=10 
        elif self.dealhand[0]=="A" and self.dealhand[1]=="A":
            self.handValue=11
        self.handValue=self.dealhand[0]+self.dealhand[1]
        return self.dealhand 
    def hit(self):
         new_card=random.sample(self.listakart,1)
         self.dealhand.extend(new_card)
         return self.dealhand
    def win(self):
        if self.handValue==21:
            print("you won")
        elif self.handValue >21:
            print("you lose")
    
    
class Dealer(BlackJack):
    def __init__(self):
        pass
    def hand(self):
        super()
    def hit(self):
        if self.handValue < 17:
            super().hit
class Player(BlackJack):
    def __init__(self):
        pass
    def hand(self):
        super()
    def hit(self):
        super().hit
       
black=BlackJack()
print(black.hand())
print(black.hit())



