from deck import *
from card import *
from setting import *

class GameController():
    def __init__(self, player):
        self.__totalReward = 0
        self.__player = player
        self.__round = 1
        self.__deck = Deck()

    def main_menu(self):
        
        # Rule
        while self.__player.get_score() >= LOSE_CONDITION and self.__player.get_score() <= WIN_CONDITION:
            print(f"Your score: {self.__player.get_score()}")
            decision = input(f'Do you want by  start game "yes" or "no" ? (y/n) : ')
            if decision == "y":
                self.__player.reduce_score(JOIN_FEE)
                print("Game is started")
                print(f"You pay 25 score. Score you : {self.__player.get_score()} ")
                self.start()
            elif decision == "n":
                break

        # End game
        if self.__player.get_score() < LOSE_CONDITION:
            print(f"You LOSE game!!!")
        elif self.__player.get_score() >= WIN_CONDITION:
            print(f"You WIN game with {self.__player.get_score()} reward!!!")

    def start(self):
        while True:

            # Round
            print(f"\t\t\t\tROUND : {self.__round.__str__()}")

            # Playing process
            house_card = self.__deck.draw_card()
            print("House's card is: " + house_card.__str__())
            playerGuess = self.__player.guess(house_card)
            self.__player.set_card(self.__deck.draw_card())
            result = Card.compare_card(self.__player.get_card(), house_card)
            print("You's card is: " + self.__player.get_card().__str__())

            # When WIN
            if((playerGuess == "greater" and result) or (playerGuess == "less" and not result)):
                print("\t\t\t\tYou win!!!")
                if(self.__totalReward):
                    self.__totalReward *= 2
                else:
                    self.__totalReward = REWARD

                if(self.__totalReward >= WIN_CONDITION):
                    self.__player.plus_score(self.__totalReward)
                    break

                # decision "continue" or "stop"
                decision = input(f'Current total reward: {self.__totalReward}, Do you want to "continue" or "stop" ? : ')
                if(decision == "stop"):
                    self.__player.plus_score(self.__totalReward)
                    self.reset_game()
                    break
                self.__round += 1
                self.reset_deck()

            # When LOSE
            else:
                print(f"\t\t\tYou LOSE game with {self.__player.get_score()} reward!!!\n\n")
                self.reset_game()
                break

    def reset_game(self):
        self.__deck = Deck()
        self.__round = 1
        self.__totalReward = 0
    
    def reset_deck(self):
        self.__deck = Deck()
        