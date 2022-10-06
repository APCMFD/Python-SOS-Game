import unittest
from main import GAME_GUI

class Test_SOS_GUI(unittest.TestCase):

    def setUp(self):
        self.game = GAME_GUI(3)
        self.game.gameboard_GUI()
        
    def tearDown(self):
        return None
      
    def test_set_r_turn(self):
        # tests making it the red player's turn
        self.game.set_r_turn()
        return self.assertEqual(self.game.current_turn.get(), self.game.R_TURN)
      
    def test_set_b_turn(self):
        # tests making it the blue player's turn
        self.game.set_b_turn()
        return self.assertEqual(self.game.current_turn.get(), self.game.B_TURN)
      
    def test_r_player_option(self):
        # tests choosing the 'S' option as the red player
        self.game.red_player.option.set('S')
        return self.assertEqual(self.game.red_player.option.get(), 'S')
      
    def test_b_player_option(self):
        # tests choosing the 'S' option as the blue player
        self.game.blue_player.option.set('S')
        return self.assertEqual(self.game.blue_player.option.get(), 'S')
      
    def test_red_move(self):
        # tests making a 'S' move as the red player in a simple game
        self.game.start_simple()
        self.game.set_r_turn()
        self.game.red_player.option.set('S')
        self.game.move(0,1)
        return self.assertEqual(self.game.board[0][1]['text'], self.game.red_player.option.get())

    def test_blue_move(self):
        # tests making a 'O' move as the blue player in a simple game
        self.game.start_simple()
        self.game.set_b_turn()
        self.game.blue_player.option.set('O')
        self.game.move(0,1)
        return self.assertEqual(self.game.board[0][1]['text'], self.game.blue_player.option.get())

    def test_invalid_move(self):
        # tests making a move over a cell that's already been used in a simple game
        self.game.start_simple()
        self.game.set_r_turn()
        self.game.red_player.option.set('S')
        self.game.move(2,2)
        
        # blue player tries to place an 'O' in the spot that the red player placed and 'S'
        self.game.blue_player.option.set('O')
        self.game.move(2,2)

        return self.assertEqual(self.game.board[2][2]['text'], 'S')
    
    def test_red_move_gen(self):
        # tests making a 'S' move as the red player in a general game
        self.game.start_general()
        self.game.set_r_turn()
        self.game.red_player.option.set('S')
        self.game.move(0,1)
        return self.assertEqual(self.game.board[0][1]['text'], self.game.red_player.option.get())

    def test_blue_move_gen(self):
        # tests making a 'O' move as the blue player in a general game
        self.game.start_general()
        self.game.set_b_turn()
        self.game.blue_player.option.set('O')
        self.game.move(0,1)
        return self.assertEqual(self.game.board[0][1]['text'], self.game.blue_player.option.get())

    def test_invalid_move_gen(self):
        # tests making a move over a cell that's already been used in a general game
        self.game.start_general()
        self.game.set_r_turn()
        self.game.red_player.option.set('S')
        self.game.move(2,2)
        
        # blue player tries to place an 'O' in the spot that the red player placed and 'S'
        self.game.blue_player.option.set('O')
        self.game.move(2,2)

        return self.assertEqual(self.game.board[2][2]['text'], 'S')

    def test_simple_game(self):
        # tests the "Simple Game" option
        self.game.start_simple()
        return self.assertEqual(self.game.gametype, self.game.SIMPLE_GAME)
      
    def test_general_game(self):
        # tests the "General Game" option
        self.game.start_general()
        return self.assertEqual(self.game.gametype, self.game.GENERAL_GAME)
        
    def test_check_if_board_not_full(self):
        # tests that the full board check is false when the board is empty
        return self.assertEqual(self.game.full_board_check(), False)
      
    def test_check_if_board_full(self):
        # tests that the full board check is true when the board is full
        for row in range(self.game.row_num):
            for col in range(self.game.col_num):
                self.game.board[row][col]['text'] = 'S'
        return self.assertEqual(self.game.full_board_check(), True)

if __name__ == '__main__':
    unittest.main()
