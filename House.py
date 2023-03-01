import random

class House:
    def __init__(self):
        self.card = None

    def draw_card(self, deck):
        self.card = random.choice(deck)
        deck.remove(self.card)
        print(f"House draws {self.card[1]} {self.card[0]}.")
class House():
    def __init__(self):
        self.__card = None
    
    def set_card(self, card):
        self.__card = card