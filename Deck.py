import random
from setting import *
from card import Card

class Deck():
    def __init__(self):
        self.__new_deck = None
        self.new_deck()

    def draw_card(self):
        card = random.choice(self.__new_deck)
        self.__new_deck.remove(card)
        return card
    
    def new_deck(self):
        self.__new_deck = []
        i = 0
        for gruop in GROUPS:
            for suite in SUITES:
                self.__new_deck.append(Card(suite, gruop, i))
                i += 1
        for suite, gruop in BIGGEST_CARD:
            self.__new_deck.append(Card(suite, gruop, i))
            i += 1

    def get_card_by(self, suite, group):
        for card in self.__new_deck:
            if card.get_suite() == suite and card.get_group() == group:
                return card
            
    def get_deck(self):
        return self.__new_deck