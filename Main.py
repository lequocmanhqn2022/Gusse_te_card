import random

SUITES = ["Spade", "Club", "Diamond", "Heart"]
GROUPS = [
        "Ace", "2", "3", 
        "4","5", "6", 
        "7", "8","9", 
        "10", "J", "Q", "K"
        ]
DECK = [(suite, group) for suite in SUITES for group in GROUPS]\
      + [("Black Joker", ""), ("Red Joker", "")]
REWARD = 20
JOIN_FEE = 25
WIN_CONDITION = 1000
LOSE_CONDITION = 30

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
        print(f"{self.name} draws {self.card[1]} {self.card[0]}.")


class House:
    def __init__(self):
        self.card = None

    def draw_card(self, deck):
        self.card = random.choice(deck)
        deck.remove(self.card)
        print(f"House draws {self.card[1]} {self.card[0]}.")


# COMPARE CARDS
def compare_cards(player_card, house_card):
    if player_card[0] not in SUITES :
        player_gruop = 13
        player_suites = 4
        house_gruop = GROUPS.index(house_card[1])
        house_suites = SUITES.index(house_card[0])
    elif house_card[0] not in SUITES:
        house_gruop = 13
        house_suites = 4
        player_gruop = GROUPS.index(player_card[1])
        player_suites = SUITES.index(player_card[0])
    else:
        player_gruop = GROUPS.index(player_card[1])
        player_suites = SUITES.index(player_card[0])
        house_gruop = GROUPS.index(house_card[1])
        house_suites = SUITES.index(house_card[0])

    if player_gruop > house_gruop:
        return "greater"
    elif player_gruop < house_gruop:
        return "less"
    else:
        if player_suites > house_suites:
            return "greater"
        else:
            return "less"
# PLAY ROUND
def round_play(player, house, deck, reward):
    player.draw_card(deck)
    house.draw_card(deck)
    result = compare_cards(player.card, house.card)
    guess = player.guess(house.card)
    if result == guess:
        print(f"Correct! {player.name} wins {reward} score."
               f"Total score: {player.score}.")
        return reward
    else:
        if reward == 20:
            reward = 0
        else:
            reward = int(reward/2)
        print(f"Wrong! {player.name} loses {reward} score."
                f"Total score: {player.score}.")
        return 0
# 
def play_game(player, house, deck, reward = REWARD):
    round = 0
    while player.score < WIN_CONDITION and player.score >= LOSE_CONDITION:
        print(f'{player.name} starts withs {player.score} score.')
        player.score -= JOIN_FEE
        print(f'{player.name} pays {JOIN_FEE} score.')
        # 
        while True and round < WIN_CONDITION:
            round = round_play(player, house, deck, reward)
            decision = input('Do you want to "continue" or "stop" ? : ')
            #
            if(decision == "continue"):
                if round == 0:
                    reward = REWARD
                else:
                    reward *= 2
                deck = DECK
            #
            else:
                player.score += round
                print(f"You stop with {player.score} score")
                while True:
                    decision = input('Do you want play game "yes" or "no" ? (y/n) : ')
                    #
                    if decision == "y":
                       reward = REWARD
                       break
                    elif decision == "n":
                       exit()
                    else:
                       print("Please enter 'y' or 'n'")
                break
        #
        else:
            player.score += round
    else:
        #
        if player.score >= WIN_CONDITION:
            print(f'{player.name},you WIN the Game.'
                   f'With {player.score} score.')
            exit()
        else:
            print(f'{player.name}, you LOSE the Game.'
                   f'With {player.score} score.')
            exit()


def main():
    play_game(Player("M"),house=House(),deck=DECK)

if __name__ == "__main__":
    main()