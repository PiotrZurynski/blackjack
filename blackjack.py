import random
class BlackJack:
    listakart=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    def __init__(self):
        pass
    def hand(self):
        self.dealhand = random.sample(self.listakart, 2)
        return self.dealhand
    def hit(self):
         new_card=random.sample(self.listakart,1)
         self.dealhand.extend(new_card)
         return self.dealhand
    
class Dealer(BlackJack):
    def __init__(self):
        pass
    def hand(self):
        super()
    def hit(self):
        if self.handValue < 17:
            super().hit
        
black=BlackJack()
print(black.hand())
print(black.hit())



