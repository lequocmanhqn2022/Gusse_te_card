from unittest.mock import MagicMock
import unittest
import builtins
from game_controller import GameController
from player import Player
from card import Card
from deck import Deck
from setting import *

class Test(unittest.TestCase):

    def test_compare_card_with_existing_cards(self):
        print("Running test_compare_card_with_existing_cards...")
        # Create some sample cards
        deck = Deck()
        card1 = deck.get_card_by("Heart","2")
        card2 = deck.get_card_by("Heart","3")
        card3 = deck.get_card_by("Diamond","2")

        # Compare cards and check the results
        self.assertFalse(Card.compare_card(card1, card2))
        self.assertTrue(Card.compare_card(card1, card3))
        self.assertTrue(Card.compare_card(card2, card3))
        print("test_compare_card_with_existing_cards passed.")

    def game_controller(self):
        player  = Player("Manh",30)
        return GameController(player)
   
    def test_game_round_win(self):
        input_values = ['y', 'coutinue']
        mock_input = MagicMock(side_effect=input_values)
        builtins.input = mock_input
        print("\n\t\t\tTest game WIN")
        game_controller = self.game_controller()
        game_controller._GameController__deck.draw_card = MagicMock(return_value= ("Hearts", "5"))
        game_controller._GameController__player.guess = MagicMock(return_value="greater")
        game_controller._GameController__player.get_card = MagicMock(return_value=("Diamonds", "10"))
        game_controller._GameController__totalReward = 250
        Card.compare_card = MagicMock(return_value=True)

        # Run the start method to check the result
        game_controller.main_menu()
        self.assertEqual(game_controller._GameController__round, 2)
        self.assertEqual(game_controller._GameController__totalReward, 1000)
        print("PASSED")

    def test_game_round_lose(self):
        input_values = 'y'
        mock_input = MagicMock(side_effect=input_values)
        builtins.input = mock_input
        print("\n\t\t\tTest game LOSE")
        game_controller = self.game_controller()
        game_controller._GameController__deck.draw_card = MagicMock(return_value= ("Hearts", "5"))
        game_controller._GameController__player.guess = MagicMock(return_value="less")
        game_controller._GameController__player.get_card = MagicMock(return_value=("Diamonds", "10"))
        Card.compare_card = MagicMock(return_value=True)

        # Run the start method to check the result
        game_controller.main_menu()
        self.assertEqual(game_controller._GameController__round, 1)
        self.assertEqual(game_controller._GameController__totalReward, 0)
        print("PASSED")

    def test_new_deck(self):
        input_values = ['y', 'countinue']
        mock_input = MagicMock(side_effect=input_values)
        builtins.input = mock_input
        print("\n\t\t\tTest new Deck")
        game_controller = self.game_controller()
        game_controller._GameController__deck.draw_card = MagicMock(return_value= ("Hearts", "5"))
        game_controller._GameController__player.guess = MagicMock(return_value="greater")
        game_controller._GameController__player.get_card = MagicMock(return_value=("Diamonds", "10"))
        game_controller._GameController__totalReward = 250
        Card.compare_card = MagicMock(return_value=True)
        print(game_controller._GameController__deck.get_deck().__len__())

        game_controller.main_menu()
        print(game_controller._GameController__deck.get_deck().__len__())
        self.assertEqual(game_controller._GameController__deck.get_deck().__len__(), 54)


if __name__ == '__main__':
    unittest.main()