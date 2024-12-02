import random
class BlackJack:
    listakart=[2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    def __init__(self):
        self.handValue=0
        self.dealhand=[]
    def hand(self):
        self.dealhand = random.sample(self.listakart, 2)
        self.handValue = self.calculate_hand_value()
        return self.dealhand   
    def calculate_hand_value(self):
        ace_count = 0
        hand_value = 0
        wartosci_kart = {"J": 10, "Q": 10, "K": 10, "A": 11}
        
        for karta in self.dealhand:
            if isinstance(karta, str):
                if karta == "A":
                    ace_count += 1
                hand_value += wartosci_kart[karta]
            else:
                hand_value += karta
                
        while hand_value > 21 and ace_count > 0:
            hand_value -= 10
            ace_count -= 1
        return hand_value
    def hit(self):
        new_card = random.choice(self.listakart)
        self.dealhand.append(new_card)
        self.handValue = self.calculate_hand_value()
        return self.dealhand
    def stand(self):
        return self.dealhand
    def win(self, player_hand_value, dealer_hand_value):
        if player_hand_value > 21:
            return "Gracz przekroczył 21, dealer wygrywa!"
        if dealer_hand_value > 21:
            return "Dealer przekroczył 21, gracz wygrywa!"
        if player_hand_value == 21:
            return "Gracz ma Blackjacka, gracz wygrywa!"
        if dealer_hand_value == 21:
            return "Dealer ma Blackjacka, dealer wygrywa!"
        if player_hand_value > dealer_hand_value:
            return "Gracz wygrywa!"
        elif dealer_hand_value > player_hand_value:
            return "Dealer wygrywa!"
        else:
            return "Remis!"
class Dealer(BlackJack):
    def __init__(self):
        super().__init__()
    def hand(self):
        super().hand()
    def hit(self):
        super().hit()
    def stand(self):
        super().stand()
    def dealer_hand(self):
        print(f"Dealer ma na ręce {self.dealhand[0]}, [X]")
    def dealer_hand_exposed(self):
        print(f"Dealer ma na ręce: ", end="")
        print(", ".join(str(karta) for karta in self.dealhand))
    
class Player(BlackJack):
    def __init__(self):
        super().__init__()
        
    def hand(self):
        super().hand()
    def hit(self):
        super().hit()
    def stand(self):
        super().stand()
    def player_hand(self):
        print(f"Player ma na ręce: ", end="")
        print(", ".join(str(karta) for karta in self.dealhand))
    
class Game:
    def __init__(self):
        self.dealer=Dealer()
        self.player=Player()

    def start_game(self):
        print("Kasynko BlackJack")
        self.dealer.hand()
        self.player.hand()
        self.dealer.dealer_hand()
        self.player.player_hand()
        if self.player.handValue==21:
            wynik=self.player.win(self.player.handValue,self.dealer.handValue)
            print(wynik)
        while self.player.handValue<21:
            print(f" Siema, hitujesz czy zostajesz?, bo masz na łapie {self.player.handValue}")
            akcja=input("Wpisz hit lub stand  ")
            if akcja.lower()=="hit":
                self.player.hit()
                self.player.player_hand()
            elif akcja.lower()=="stand":
                self.player.stand()
                self.player.player_hand()
                print("Koniec tury")
                break
        
        if self.player.handValue >21:
            print("ojć too much")
            return  
        self.dealer.dealer_hand_exposed()
        while self.dealer.handValue < 17:
            self.dealer.hit()
            print(f"Dealer ma teraz rękę {self.dealer.dealhand} o wartości {self.dealer.handValue}")
        print(f"Gracz ma {self.player.dealhand} o wartości {self.player.handValue}")
        print(f"Dealer ma {self.dealer.dealhand} o wartości {self.dealer.handValue}")
        result = self.dealer.win(self.player.handValue, self.dealer.handValue)
        print(result)

        self.play_again()

    def play_again(self):
        again = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ").lower()
        if again == "tak":
            self.start_game()
        else:
            print("Dziękujemy za grę!")

if __name__ =="__main__":
    game=Game()
    game.start_game()



