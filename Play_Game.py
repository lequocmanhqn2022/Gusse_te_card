from game_controller import *
from player import *

def main():
    while True:
        try:
            name = input("Enter your name: ")
            if name.isalpha():
                break
            else:
                raise ValueError
        except ValueError:
            print("Names can only contain letters, try again!")
    gameController = GameController(Player(name))
    gameController.main_menu()

if __name__ == "__main__":
    main()