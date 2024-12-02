import random
class BlackJack:
    listakart=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    handValue=0
    def __init__(self):
        pass
    def hand(self):
        self.dealhand = random.sample(self.listakart, 2) 
        self.handValue = 0  
        ace_count = 0  
        wartosci_kart = {"J": 10, "Q": 10, "K": 10, "A": 11}
        for karta in self.dealhand:
            if isinstance(karta, str): 
                if karta == "A":
                    ace_count += 1  
                self.handValue += wartosci_kart[karta] 
            else:  
                self.handValue += karta
        while self.handValue > 21 and ace_count > 0:
            self.handValue -= 10  
            ace_count -= 1  
        return self.handValue
    def hit(self):
         new_card=random.sample(self.listakart,1)
         self.dealhand.extend(new_card)
         return self.dealhand
    def stand(self):
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
    def stand(self):
        if self.handValue >=17:
            super().stand
class Player(BlackJack):
    def __init__(self):
        pass
    def hand(self):
        super()
    def hit(self):
        super().hit
    def stand(self):
        super().stand
       
black=BlackJack()
print(black.hand())
print(black.hit())
print(black.stand())



