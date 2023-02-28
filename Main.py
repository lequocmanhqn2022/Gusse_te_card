import random, House, Player

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
        print(f"{player.name} draws {player.card[1]} {player.card[0]}.")
        print(f"Correct! {player.name} wins {reward} score."
               f"Total score: {player.score}.")
        return reward
    else:
        if reward == 20:
            reward = 0
        else:
            reward = int(reward/2)
        print(f"{player.name} draws {player.card[1]} {player.card[0]}.")
        print(f"Wrong! {player.name} loses {reward} score."
                f"Total score: {player.score}.")
        return 0
# 
def play_game(player, house, deck, reward = REWARD):
    reward_round = reward
    round = 1
    #
    while player.score < WIN_CONDITION and player.score >= LOSE_CONDITION:
        print(f'{player.name} starts withs {player.score} score.')
        player.score -= JOIN_FEE
        print(f'{player.name} pays {JOIN_FEE} score.')
        # 
        while True and reward_round < WIN_CONDITION:
            print(f'ROUND {round} : {reward} score.')
            reward_round = round_play(player, house, deck, reward)
            #
            if reward_round == 0:
                while True:
                    decision = input('Do you want play game "yes" or "no" ? (y/n) : ')
                    #
                    if decision == "y":
                       print("\n")
                       reward = REWARD
                       break
                    elif decision == "n":
                       exit()
                    else:
                       print("Please enter 'y' or 'n'")
                break
            #
            decision = input('Do you want to "continue" or "stop" ? : ')
            print("\n")
            #
            if(decision == "continue"):
                if reward_round == 0:
                    reward = REWARD
                    round = 1
                else:
                    reward *= 2
                    round += 1
                deck = DECK
            #
            else:
                round = 1
                player.score += reward_round
                print(f"You stop with {player.score} score")
                while True:
                    decision = input('Do you want play game "yes" or "no" ? (y/n) : ')
                    #
                    if decision == "y":
                       print("\n")
                       reward = REWARD
                       break
                    elif decision == "n":
                       exit()
                    else:
                       print("Please enter 'y' or 'n'")
                break
        #
        else:
            player.score += reward_round
    #
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
    play_game(Player.Player("M"),house=House.House(),deck=DECK)

if __name__ == "__main__":
    main()