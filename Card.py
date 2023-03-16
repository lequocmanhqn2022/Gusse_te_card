class Card():
    def __init__(self, suite, group, compareValue):
        self.__suite = suite
        self.__group = group
        self.__compare_value = compareValue

    def get_suite(self):
        return self.__suite
    
    def get_group(self):
        return self.__group
    
    def get_compare_value(self):
        return self.__compare_value
    
    def __str__(self):
        return f'{self.__group}({self.__suite})'
    
    def compare_card(card1, card2):
        return card1.get_compare_value() > card2.get_compare_value()
    
# Static method
Card.compare_card = staticmethod(Card.compare_card)
