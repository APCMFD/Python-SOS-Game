import unittest
import constant
from sprint5 import GAME_GUI

class Test_SOS_GUI(unittest.TestCase):

    def setUp(self):
        # called when unittest is run
        self.gameGUI = GAME_GUI()
        self.gameGUI.BOARD_SIZE = 5
        self.gameGUI.game_info()
        self.gameGUI.gameboard_GUI()
        
    def tearDown(self):
        # called when uittest ends
        return None
      
    def test_red_human(self):
        # tests selecting "human" for the red player
        self.gameGUI.game.set_red_human()
        return self.assertEqual(self.gameGUI.game.red_player.type, constant.HUMAN)

    def test_blue_human(self):
        # tests selecting "human" for the blue player
        self.gameGUI.game.set_blue_human()
        return self.assertEqual(self.gameGUI.game.blue_player.type, constant.HUMAN)

    def test_red_computer(self):
        # tests selecting "computer" for the red player
        self.gameGUI.game.set_red_computer(self.gameGUI.gameboard)
        return self.assertEqual(self.gameGUI.game.red_player.type, constant.COMPUTER)

    def test_blue_computer(self):
        # tests selecting "computer" for the blue player
        self.gameGUI.game.set_blue_computer(self.gameGUI.gameboard)
        return self.assertEqual(self.gameGUI.game.blue_player.type, constant.COMPUTER)

    def test_computer_option(self):
        # tests the computer's ability to select a random option between 'S' and 'O'
        self.gameGUI.game.set_red_computer(self.gameGUI.gameboard)
        option = self.gameGUI.game.red_player.option_choice()
        return self.assertEqual(option, self.gameGUI.game.red_player.get_option())

    def test_computer_move(self):
        # tests the computer making a move
        self.gameGUI.game.set_red_computer(self.gameGUI.gameboard)
        row, col = self.gameGUI.game.red_player.choose_cell(self.gameGUI.gameboard)
        self.gameGUI.game.red_player.move(self.gameGUI.gameboard, row, col)
        return self.assertEqual(self.gameGUI.gameboard.get_symbol(row, col), self.gameGUI.game.red_player.get_option())

    def test_simple_game(self):
        # tests the simple game option
        self.gameGUI.start_simple()
        return self.assertEqual(self.gameGUI.game.type, constant.SIMPLE_GAME)

    def test_general_game(self):
        # tests the general game option
        self.gameGUI.start_general()
        return self.assertEqual(self.gameGUI.game.type, constant.GENERAL_GAME)

    def test_red_move(self):
        # tests the red player placing an 'S' in a simple game
        self.gameGUI.start_simple()
        self.gameGUI.game.set_red()
        self.gameGUI.game.red_player.set_option('S')
        self.gameGUI.game.game_check(self.gameGUI.gameboard, 2, 2)
        return self.assertEqual(self.gameGUI.gameboard.get_symbol(2, 2), self.gameGUI.game.red_player.get_option())

    def test_blue_move(self):
        # tests the blue player placing an 'O' in a general game
        self.gameGUI.start_general()
        self.gameGUI.game.set_blue()
        self.gameGUI.game.blue_player.set_option('O')
        self.gameGUI.game.game_check(self.gameGUI.gameboard, 2, 2)
        return self.assertEqual(self.gameGUI.gameboard.get_symbol(2, 2), self.gameGUI.game.blue_player.get_option())

    def test_simple_game_over(self):
        # tests the an 'SOS' forming on a red player's turn to end a simple game where the red player wins
        self.gameGUI.start_simple()
        self.gameGUI.game.set_red()
        self.gameGUI.game.red_player.set_option('S')
        self.gameGUI.gameboard.set_symbol(0, 1, 'S')
        self.gameGUI.gameboard.set_symbol(1, 1, 'O')
        self.gameGUI.game.game_check(self.gameGUI.gameboard, 2, 1)
        return self.assertEqual(self.gameGUI.game.red_wins, 1)

    def test_general_game_over(self):
        # tests the blue player forming an 'SOS' after the rest of the board is filled with several 'O' to end a general game where the blue player wins
        self.gameGUI.start_general()
        self.gameGUI.game.set_blue()
        self.gameGUI.game.blue_player.set_option('S')
        self.gameGUI.gameboard.set_symbol(0, 1, 'S')
        self.gameGUI.gameboard.set_symbol(1, 1, 'O')
        self.gameGUI.game.game_check(self.gameGUI.gameboard, 2, 1)
        for row in range(self.gameGUI.gameboard.board_size):
            for col in range(self.gameGUI.gameboard.board_size):
                if row != 3 or col != 3:
                    if self.gameGUI.gameboard.get_symbol(row, col) == constant.EMPTY:
                        self.gameGUI.gameboard.set_symbol(row, col, 'O')
        self.gameGUI.game.game_check(self.gameGUI.gameboard, 3, 3)
        return self.assertEqual(self.gameGUI.game.blue_wins, 1)


if __name__ == '__main__':
    unittest.main()
