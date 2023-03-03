from CardSet import *
from Card import *


class GameController():
    def __init__(self, player):
        self.__totalReward = 0
        self.__player = player
        self.__cardSet = CardSet()

    def main_menu(self):
        while True:
            print(f"Your score: {self.__player.get_score()}")
            decision = input('Do you want start game "yes" or "no" ? (y/n) : ')
            if decision == "y":
                if(self.__player.get_score() < 25):
                    print("You LOSE game")
                    break
                self.__player.reduce_score(25)
                print("Game is started")
                self.start()
            elif decision == "n":
                break

    def start(self):
        while True:
            house_card = self.__cardSet.draw_card()
            print("House's card is: " + house_card.__str__())
            playerGuess = self.__player.guess(house_card)
            self.__player.set_card(self.__cardSet.draw_card())
            result = Card.compare_card(self.__player.get_card(), house_card)
            if((playerGuess == "greater" and result) or (playerGuess == "less" and not result)):
                print("You's card is: " + self.__player.get_card().__str__())
                print("You win!!!")
                # when win
                if(self.__totalReward):
                    self.__totalReward *= 2
                else:
                    self.__totalReward = 20
                print(self.__totalReward)
                if(self.__totalReward >= 1000):
                    self.__player.plus_score(1000)
                    self.reset()
                    print("You win game with 1000 reward!!!")
                    break
                decision = input(f'Current total reward: {self.__totalReward}, Do you want to "continue" or "stop" ? : ')
                if(decision == "stop"):
                    self.__player.plus_score(self.__totalReward)
                    self.reset()
                    break
            else:
                print("You's card is: " + self.__player.get_card().__str__())
                print("You lose!!!")
                self.reset()
                break

    def reset(self):
        self.__cardSet = CardSet()
        self.__totalReward = 0
    