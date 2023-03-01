
class Player():
    def __init__(self, name, score = 60):
        self.__name = name
        self.__score = score
        self.__card = None

    def guess(self, house_card):
        guess = input(f"{self.__name}, do you think your card is greater or less "
                      f"than {house_card.get_group()} {house_card.get_suite()}? (Enter 'greater' or 'less'): ")
        return guess
    
    def set_card(self, card):
        self.__card = card

    def get_card(self):
        return self.__card

    def get_score(self):
        return self.__score

    def plus_score(self, score):
        self.__score += score

    def reduce_score(self, score):
        self.__score -= score
        
        