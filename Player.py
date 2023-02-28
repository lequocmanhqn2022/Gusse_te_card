import random

class Player:
    def __init__(self, name, score = 60):
        self.name = name
        self.score = score
        self.card = None

    def guess(self, house_card):
        guess = input(f"{self.name}, do you think your card is greater or less "
                      f"than {house_card[1]} {house_card[0]}? (Enter 'greater' or 'less'): ")
        return guess
    
    def draw_card(self, deck):
        self.card = random.choice(deck)
        deck.remove(self.card)