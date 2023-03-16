from unittest.mock import MagicMock
import unittest
from GameController import GameController
from Player import Player
from Card import Card
from Deck import Deck
from Setting import *

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


if __name__ == '__main__':
    unittest.main()