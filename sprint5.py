from tkinter import *
from tkinter import messagebox
from datetime import datetime
import random
import constant
import json

class GAME_BOARD():
    # class used for creating the game board based on chosen board size

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = []
        self.create_skeleton()
        
    def create_skeleton(self):
        # creates empty board
        for row in range(self.board_size):
            self.board.append([])
            for col in range(self.board_size):
                self.board[row].append(0)
                
    def get_board_size(self):
        # returns the board size
        return self.board_size

    def get_symbol(self, row, col):
        # returns the symbol in a given cell
        return self.board[row][col]['text']

    def set_symbol(self, row, col, symbol):
        # sets the symbol in a given cell
        self.board[row][col]['text'] = symbol
    
    def reset_board(self):
        # returns board to initial state
        for r in range(self.board_size):
            for c in range(self.board_size):
                tile = self.board[r][c]
                tile['text'] = ' '
                tile['bg'] = 'white'
                
    def full_board_check(self):
        # used to check if the board is full
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col]['text'] == ' ':
                    return False
        return True
    
    def middle_check(self, move_row, move_col, player_color):
        # checks to see if the most recent move is the middle character in one or more 'SOS'
        move_tile = self.board[move_row][move_col]
        sos_num = 0
        try:
            if (move_col - 1) < 0:
                pass
            elif self.board[move_row][move_col-1]['text'] == 'S' and self.board[move_row][move_col+1]['text'] == 'S':
                # looks for a horizontal 'SOS'
                if player_color != 'white':
                    self.board[move_row][move_col-1]['bg'] = player_color
                    self.board[move_row][move_col+1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0:
                pass
            elif self.board[move_row-1][move_col]['text'] == 'S' and self.board[move_row+1][move_col]['text'] == 'S':
                # looks for a vertical 'SOS'
                if player_color != 'white':
                    self.board[move_row-1][move_col]['bg'] = player_color
                    self.board[move_row+1][move_col]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_col - 1) < 0:
                pass
            elif self.board[move_row+1][move_col-1]['text'] == 'S' and self.board[move_row-1][move_col+1]['text'] == 'S':
                # looks for a diagonal 'SOS' that is going up toward the right
                if player_color != 'white':
                    self.board[move_row+1][move_col-1]['bg'] = player_color
                    self.board[move_row-1][move_col+1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_col - 1) < 0:
                pass
            elif self.board[move_row-1][move_col-1]['text'] == 'S' and self.board[move_row+1][move_col+1]['text'] == 'S':
                # looks for a diagonal 'SOS' that is going down toward the right
                if player_color != 'white':
                    self.board[move_row-1][move_col-1]['bg'] = player_color
                    self.board[move_row+1][move_col+1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        return sos_num
    
    def right_check(self, move_row, move_col, player_color):
        # checks to see if the most recent move is the right character in one or more 'SOS'
        move_tile = self.board[move_row][move_col]
        sos_num = 0
        try:
            if (move_col - 1) < 0 or (move_col - 2) < 0:
                pass
            elif self.board[move_row][move_col-2]['text'] == 'S' and self.board[move_row][move_col-1]['text'] == 'O':
                # looks for a horizontal 'SOS'
                if player_color != 'white':
                    self.board[move_row][move_col-2]['bg'] = player_color
                    self.board[move_row][move_col-1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_row - 2) < 0:
                pass
            elif self.board[move_row-2][move_col]['text'] == 'S' and self.board[move_row-1][move_col]['text'] == 'O':
                # looks for a vertical 'SOS'
                if player_color != 'white':
                    self.board[move_row-2][move_col]['bg'] = player_color
                    self.board[move_row-1][move_col]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if (move_col - 1) < 0 or (move_col - 2) < 0:
                pass
            elif self.board[move_row+2][move_col-2]['text'] == 'S' and self.board[move_row+1][move_col-1]['text'] == 'O':
                # looks for a diagonal 'SOS' that is going up toward the right
                if player_color != 'white':
                    self.board[move_row+2][move_col-2]['bg'] = player_color
                    self.board[move_row+1][move_col-1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_row - 2) < 0 or (move_col - 1) < 0 or (move_col - 2) < 0:
                pass
            elif self.board[move_row-2][move_col-2]['text'] == 'S' and self.board[move_row-1][move_col-1]['text'] == 'O':
                # looks for a diagonal 'SOS' that is going down toward the right
                if player_color != 'white':
                    self.board[move_row-2][move_col-2]['bg'] = player_color
                    self.board[move_row-1][move_col-1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        return sos_num
    
    def left_check(self, move_row, move_col, player_color):
        # checks to see if the most recent move is the left character in one or more 'SOS'
        move_tile = self.board[move_row][move_col]
        sos_num = 0
        try:
            if self.board[move_row][move_col+2]['text'] == 'S' and self.board[move_row][move_col+1]['text'] == 'O':
                # looks for a horizontal 'SOS'
                if player_color != 'white':
                    self.board[move_row][move_col+2]['bg'] = player_color
                    self.board[move_row][move_col+1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if self.board[move_row+2][move_col]['text'] == 'S' and self.board[move_row+1][move_col]['text'] == 'O':
                # looks for a vertical 'SOS'
                if player_color != 'white':
                    self.board[move_row+2][move_col]['bg'] = player_color
                    self.board[move_row+1][move_col]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if (move_row - 1) < 0 or (move_row - 2) < 0:
                pass
            elif self.board[move_row-2][move_col+2]['text'] == 'S' and self.board[move_row-1][move_col+1]['text'] == 'O':
                # looks for a diagonal 'SOS' that is going up toward the right
                if player_color != 'white':
                    self.board[move_row-2][move_col+2]['bg'] = player_color
                    self.board[move_row-1][move_col+1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        try:
            if self.board[move_row+2][move_col+2]['text'] == 'S' and self.board[move_row+1][move_col+1]['text'] == 'O':
                # looks for a diagonal 'SOS' that is going down toward the right
                if player_color != 'white':
                    self.board[move_row+2][move_col+2]['bg'] = player_color
                    self.board[move_row+1][move_col+1]['bg'] = player_color
                    move_tile['bg'] = player_color
                sos_num += 1
        except IndexError:
            pass
        return sos_num

    def game_check(self, move_row, move_col, player_color):
        # in a simple game, checks to see if any 'SOS' has formed and the game has been won. Looks for number of created 'SOS' to update the scores in a general game.
        symbol = self.board[move_row][move_col]['text']

        if symbol == 'O':
            sos_num = self.middle_check(move_row, move_col, player_color)
            return sos_num
        elif symbol == 'S':
            sos_num = self.right_check(move_row, move_col, player_color) + self.left_check(move_row, move_col, player_color)
            return sos_num
        else:
            return 0

class SimpleGame():
    def __init__(self):
        self.type = constant.SIMPLE_GAME
        self.red_player = Player("Red Player", "red")
        self.blue_player = Player("Blue Player", "blue")
        self.red_type = StringVar()
        self.blue_type = StringVar()
        self.red_type.set(constant.HUMAN)
        self.blue_type.set(constant.HUMAN)
        self.current_turn = StringVar()
        self.current_player = self.red_player
        self.record_option = False
        self.red_wins = 0
        self.blue_wins = 0

    def set_record(self):
        # changes whether or not the game is being recorded after the record button is pressed
        if self.record_option:
            self.record_option = False
        elif not self.record_option:
            self.record_option = True

    def record_game(self, winner, gameboard):
        # writes the date and time, board size, and the winner (or DRAW) to the "game_records.txt" file
        board_size = gameboard.get_board_size()
        now = datetime.now()
        date_string = now.strftime("%m%d%Y %H:%M:%S")

        with open('game_records.txt', 'a') as file:
            if winner == constant.DRAW:
                data_line = {'date_time': date_string, 'gametype': constant.SIMPLE_GAME, 'board_size': board_size, 'winner': constant.DRAW}
                file.write(json.dumps(data_line))
                file.write('\n')
            else:
                winner_name = winner.get_name()
                data_line = {'date_time': date_string, 'gametype': constant.SIMPLE_GAME, 'board_size': board_size, 'winner': winner_name}
                file.write(json.dumps(data_line))
                file.write('\n')

    def add_win(self, winner):
        # increments the number of wins for the winning player
        if winner == self.red_player:
            self.red_wins += 1
        elif winner == self.blue_player:
            self.blue_wins += 1

    def reset(self, gameboard, winner):
        # called when a game is reset
        if self.record_option and winner != constant.NULL:
            self.record_game(winner, gameboard)
        gameboard.reset_board()
        self.check_player_comp()
        self.red_player.reset_sos()
        self.blue_player.reset_sos()
        self.set_red(gameboard)

    def set_red_human(self):
        # sets the red player to be a human player
        self.red_type.set(constant.HUMAN)
        self.red_player = Player("Red Player", "red")

    def set_blue_human(self):
        # sets the blue player to be a human player
        self.blue_type.set(constant.HUMAN)
        self.blue_player = Player("Blue Player", "blue")

    def set_red_computer(self, gameboard):
        # sets the red player to be a computer player
        self.red_type.set(constant.COMPUTER)
        if self.current_player.get_name() == self.red_player.get_name():
            self.red_player = Computer("Red Player", "red")
            self.set_red(gameboard)
        else:
            self.red_player = Computer("Red Player", "red")

    def set_blue_computer(self, gameboard):
        # sets the blue player to be a computer player
        self.blue_type.set(constant.COMPUTER)
        if self.current_player.get_name() == self.blue_player.get_name():
            self.blue_player = Computer("Blue Player", "blue")
            self.set_blue(gameboard)
        else:
            self.blue_player = Computer("Blue Player", "blue")

    def set_red(self, gameboard=constant.NULL):
        # sets the current turn to the red player
        self.current_turn.set('Current Turn: Red Player')
        self.current_player = self.red_player
        if self.current_player.type == constant.COMPUTER:
            row, col = self.current_player.choose_cell(gameboard)
            self.game_check(gameboard, row, col)
        
    def set_blue(self, gameboard=constant.NULL):
        # sets the current turn to the blue player
        self.current_turn.set('Current Turn: Blue Player')
        self.current_player = self.blue_player
        if self.current_player.type == constant.COMPUTER:
            row, col = self.current_player.choose_cell(gameboard)
            self.game_check(gameboard, row, col)

    def change_turn(self, gameboard):
        # changes which player is the current player
        if self.current_player == self.red_player:
            self.set_blue(gameboard)
        elif self.current_player == self.blue_player:
            self.set_red(gameboard)

    def game_check(self, gameboard, row, col):
        # checks to see if the game is over or not and acts accordingly
        if self.current_player.move(gameboard, row, col) == constant.GOOD_MOVE:
            board_game_status = gameboard.game_check(row, col, self.current_player.color)
            if board_game_status > 0:
                winner = self.current_player
                self.win_message(self.current_player)
                self.add_win(winner)
                self.reset(gameboard, winner)
                return constant.NULL

            if gameboard.full_board_check():
                winner = constant.DRAW
                self.draw_message()
                self.reset(gameboard, winner)
                return constant.NULL
            else:
                self.change_turn(gameboard)
                return constant.NULL

    def win_message(self, winner):
        # message that displays if a player wins
        messagebox.showinfo('Winner', f'{winner.get_name()} wins!')

    def draw_message(self):
        # message that displays for a draw
        messagebox.showinfo('Draw', 'This game has ended in a draw.')

    def check_player_comp(self):
        # checks to see if players are both computers at the end of a game. If so, they are reset to being human players
        if self.red_player.type == constant.COMPUTER and self.blue_player.type == constant.COMPUTER:
            messagebox.showinfo('Players Reset', 'Both players have been reset to \'Human\'')
            self.set_red_human()
            self.set_blue_human()

class GeneralGame(SimpleGame):
    # subclass of the SimpleGame class for the general game type.
    def __init__(self):
        super().__init__()
        self.type = constant.GENERAL_GAME

    def record_game(self, winner, gameboard):
        # writes the date and time, board size, the players' scores, and the winner (or DRAW) to the "game_records.txt" file
        board_size = gameboard.get_board_size()
        red_sos = self.red_player.get_sos()
        blue_sos = self.blue_player.get_sos()
        now = datetime.now()
        date_string = now.strftime("%m%d%Y %H:%M:%S")

        with open('game_records.txt', 'a') as file:
            if winner == constant.DRAW:
                data_line = {'date_time': date_string, 'gametype': constant.GENERAL_GAME, 'board_size': board_size, 'red_sos_count': red_sos, 'blue_sos_count': blue_sos, 'winner': constant.DRAW}
                file.write(json.dumps(data_line))
                file.write('\n')
            else:
                winner_name = winner.get_name()
                data_line = {'date_time': date_string, 'gametype': constant.GENERAL_GAME, 'board_size': board_size, 'red_sos_count': red_sos, 'blue_sos_count': blue_sos, 'winner': winner_name}
                file.write(json.dumps(data_line))
                file.write('\n')

    def get_winner(self):
        # determine the winner when the game is over (if there is a winner)
        if self.red_player.get_sos() > self.blue_player.get_sos():
            return self.red_player
        elif self.blue_player.get_sos() > self.red_player.get_sos():
            return self.blue_player
        else:
            return constant.DRAW

    def game_check(self, gameboard, row, col):
        # checks to see if the game is over or not and acts accordingly
        if row == constant.FULL_BOARD:
            winner = self.get_winner()
            if winner == constant.DRAW:
                self.draw_message()
                self.reset(gameboard, winner)
                return constant.NULL
            else:
                self.add_win(winner)
                self.win_message(winner)
                self.reset(gameboard, winner)
                return constant.NULL
            
        if self.current_player.move(gameboard, row, col) == constant.GOOD_MOVE:
            board_game_status = gameboard.game_check(row, col, self.current_player.color)
            if board_game_status > 0:
                self.current_player.add_sos(board_game_status)
                self.check_if_comp(gameboard)
            else:
                self.change_turn(gameboard)

            if gameboard.full_board_check():
                winner = self.get_winner()
                if winner == constant.DRAW:
                    self.draw_message()
                    self.reset(gameboard, winner)
                else:
                    self.add_win(winner)
                    self.win_message(winner)
                    self.reset(gameboard, winner)

        return constant.NULL

    def check_if_comp(self, gameboard):
        # checks if a player is a computer player after earning a point. Computer goes again if so
        if self.current_player.type == constant.COMPUTER:
            row, col = self.current_player.choose_cell(gameboard)
            self.game_check(gameboard, row, col)

    def win_message(self, winner):
        # message that displays when a player wins
        messagebox.showinfo('Winner', f'{winner.get_name()} wins with {winner.get_sos()} points!\nRed Player\'s SOS count: {self.red_player.get_sos()}\nBlue Player\'s SOS count: {self.blue_player.get_sos()}')

class Player():
    # class used for each player
    
    def __init__(self, name, color):
        self.name = StringVar()
        self.type = constant.HUMAN
        self.color = color
        self.option = StringVar()
        self.sos_num = 0
        self.set_name(name)
        self.set_option('S')

    def set_name(self, name):
        # sets the object's name
        self.name.set(name)

    def get_name(self):
        # returns the object's name
        return self.name.get()

    def set_option(self, option):
        # sets which letter the player is using
        self.option.set(option)
        
    def get_option(self):
        # used to check if player has selected 'S' or 'O'
        return self.option.get()

    def add_sos(self, sos_count):
        # increments the number of 'SOS' the player has by the number of 'SOS' created on this turn
        self.sos_num += sos_count

    def reset_sos(self):
        # return the number of 'SOS' teh player has to 0
        self.sos_num = 0

    def get_sos(self):
        # used to check the number of 'SOS' the player has
        return self.sos_num

    def move(self, gameboard, row, col):
        # function called when player makes a move. Shows error if invalid move is made.
        if gameboard.get_symbol(row, col) != constant.EMPTY:
            messagebox.showerror('Invalid Move', 'This cell is already occupied. Select an empty cell.')
            return constant.BAD_MOVE
        else:
            gameboard.set_symbol(row, col, self.get_option())
            return constant.GOOD_MOVE

class Computer(Player):
    # subclass of the player class for computer players
    
    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = constant.COMPUTER

    def option_choice(self):
        # randomly selects either 'S' or 'O'
        random_option = random.choice(['S', 'O'])
        self.set_option(random_option)
        return random_option

    def random_row_and_col(self, gameboard):
        # selects a random row and column
        random_row = random.randrange(0, gameboard.get_board_size())
        random_col = random.randrange(0, gameboard.get_board_size())
        return random_row, random_col

    def choose_cell(self, gameboard):
        # looks for a good cell to place the computer's chosen option
        if gameboard.full_board_check():
            return constant.FULL_BOARD, constant.FULL_BOARD
        else:
            options = ['S', 'O']
            for option in options:
                self.set_option(option)
                for row in range(gameboard.board_size):
                    for col in range(gameboard.board_size):
                        if gameboard.get_symbol(row, col) != constant.EMPTY:
                            continue
                        else:
                            if option == 'S':
                                if gameboard.right_check(row, col, 'white') > 0 or gameboard.left_check(row, col, 'white') > 0:
                                    return row, col
                            elif option == 'O':
                                if gameboard.middle_check(row, col, 'white') > 0:
                                    return row, col
                                
            option = self.option_choice()
            while(gameboard.get_symbol(row, col) != constant.EMPTY):
                row, col = self.random_row_and_col(gameboard)

            return row, col


    def move(self, gameboard, row, col):
        # called when a computer player makes a move
        gameboard.set_symbol(row, col, self.get_option())
        return constant.GOOD_MOVE
   
class GAME_GUI():
    # class used for the SOS game's GUI
    
    def __init__(self):
        self.WIN = Tk()
        self.WIN_WIDTH = 400
        self.WIN_HEIGHT = 400
        self.infoWindow = constant.EMPTY
        self.WIN_TITLE = 'SOS'
        self.WIN.title(self.WIN_TITLE)
        self.BUTTON_HEIGHT = 4
        self.BUTTON_WIDTH = 8
        self.BOARD_SIZE = constant.EMPTY
        self.WIN.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.start_button = Button(self.WIN, height=4, width=10, text='START', command=lambda:self.game_info())
        self.start_button.pack()
        self.gametype = StringVar()
        self.gameboard = constant.EMPTY
        self.game = SimpleGame()
        self.size_entry = constant.EMPTY
        
    def start(self):
        # displays window
        self.WIN.mainloop()

    def exit_window(self):
        # called when exiting the window
        self.WIN.quit()
        self.WIN.destroy()

    def game_info(self):
        # returns the relevant information about the current game
        self.start_button.pack_forget()
        self.infoWindow = Toplevel(self.WIN)
        self.infoWindow.title("Choose a board size and game type")
        self.infoWindow.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        size_label = Label(self.infoWindow, text="Enter a board size (must be > 2)")
        size_label.pack()
        self.size_entry = Entry(self.infoWindow)
        self.size_entry.pack()
        simple_button = Radiobutton(self.infoWindow, text='Simple Game', variable=self.gametype, value=constant.SIMPLE_GAME, command=lambda: self.start_simple())
        simple_button.pack()
        general_button = Radiobutton(self.infoWindow, text='General Game', variable=self.gametype, value=constant.GENERAL_GAME, command=lambda: self.start_general())
        general_button.pack()
        begin_button = Button(self.infoWindow, height=4, width=10, text="Start Game", command=lambda:self.check_info())
        begin_button.pack()
        replay_button = Button(self.infoWindow, height=4, width=15, text='Replay Last Game', command=lambda:self.replay_game())
        replay_button.pack()
        simple_button.select()

    def check_info(self):
        # checks the size that the user enters to make sure it is valid before creating the gameboard GUI
        try:
            board_size = self.size_entry.get()
            self.BOARD_SIZE = int(board_size)
        except ValueError:
            messagebox.showerror('Invalid Board Size', 'Enter an integer that is greater than 2.')
            return None
        
        if self.BOARD_SIZE < 3:
            messagebox.showerror('Invalid Board Size', 'Enter an integer that is greater than 2.')
            return None
        else:
            self.gameboard_GUI()

    def start_simple(self):
        # sets the gametype to "simple game"
        self.game = SimpleGame()
        
    def start_general(self):
        # sets the gametype to "general game"
        self.game = GeneralGame()

    def replay_game(self):
        try:
            with open('game_records.txt', 'r') as file:
                record_list = file.readlines()
                last_game = json.loads(record_list[-1])
                self.BOARD_SIZE = last_game['board_size']
                

                if last_game['gametype'] == constant.SIMPLE_GAME:
                    self.start_simple()
                    self.gametype.set(constant.SIMPLE_GAME)
                elif last_game['gametype'] == constant.GENERAL_GAME:
                    self.start_general()
                    self.gametype.set(constant.GENERAL_GAME)

                self.gameboard_GUI()

        except FileNotFoundError:
            messagebox.showerror("Game Records File Not Found", "game_records.txt could not be found. Try starting a new game.")
            return constant.NULL
            
    def gameboard_GUI(self):
        # creates the GUI for the gameboard
        self.infoWindow.destroy()
        self.WIN.title(self.gametype.get())
        self.gameboard = GAME_BOARD(self.BOARD_SIZE)
        self.GAME_WIDTH = (self.BUTTON_WIDTH * self.BOARD_SIZE) * 25
        self.GAME_HEIGHT = (self.BUTTON_HEIGHT * self.BOARD_SIZE) * 25
        self.WIN.geometry(f"{self.GAME_WIDTH}x{self.GAME_HEIGHT}")
        
        # creates the buttons that fill up the gameboard
        for r in range(self.BOARD_SIZE):
            for c in range(self.BOARD_SIZE):
                tile = self.gameboard.board[r][c] = Button(
                    self.WIN, bg="white", text=constant.EMPTY, height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda row1=r, col1=c: self.game.game_check(self.gameboard, row1, col1))
                tile.grid(row=r, column=c, padx=2, pady=2)

        # creates the label for the current turn
        turn_label = Label(self.WIN, textvariable=self.game.current_turn)
        turn_label.grid(row=0, column=self.BOARD_SIZE+1)
                
        # creates restart button
        restart_game_button = Button(
            self.WIN, text='Restart Game', command=lambda: self.game.reset(self.gameboard, constant.NULL))
        restart_game_button.grid(row=6, column=self.BOARD_SIZE+4)

        # creates record checkbox
        record_checkbox = Checkbutton(self.WIN, text='Record Game', variable=self.game.record_option, command=lambda: self.game.set_record())
        record_checkbox.grid(row=6, column=self.BOARD_SIZE+2)
        
        # frames for the player labels
        red_frame = Frame(self.WIN)
        blue_frame = Frame(self.WIN)

        # creates the player labels
        red_label = Label(red_frame, text='Red Player')
        blue_label = Label(blue_frame, text='Blue Player')

        # creates radio buttons for selecting if a player is human
        red_human_button = Radiobutton(red_frame, text='Human', variable=self.game.red_type, value=constant.HUMAN, command=lambda: self.game.set_red_human())
        blue_human_button = Radiobutton(blue_frame, text='Human', variable=self.game.blue_type, value=constant.HUMAN, command=lambda: self.game.set_blue_human())

        red_frame.grid(row=1, column=self.BOARD_SIZE+2)
        blue_frame.grid(row=1, column=self.BOARD_SIZE+3)

        red_label.pack(side="top")
        blue_label.pack(side="top")
        red_human_button.pack(side="top")
        blue_human_button.pack(side="top")

        # creates frames for the option selection for each player
        red_option_frame = Frame(self.WIN)
        blue_option_frame = Frame(self.WIN)

        # creates the 'S' and 'O' buttons for both players
        red_S_button = Radiobutton(
            red_option_frame, text='S', variable=self.game.red_player.option, value='S', command=lambda: self.game.red_player.set_option('S'))
        red_O_button = Radiobutton(
            red_option_frame, text='O', variable=self.game.red_player.option, value='O', command=lambda: self.game.red_player.set_option('O'))
        
        blue_S_button = Radiobutton(
            blue_option_frame, text='S', variable=self.game.blue_player.option, value='S', command=lambda: self.game.blue_player.set_option('S'))
        blue_O_button = Radiobutton(
            blue_option_frame, text='O', variable=self.game.blue_player.option, value='O', command=lambda: self.game.blue_player.set_option('O'))

        red_option_frame.grid(row=2, column=self.BOARD_SIZE+2)
        blue_option_frame.grid(row=2, column=self.BOARD_SIZE+3)
        red_S_button.pack(side="top")
        red_O_button.pack(side="top")
        blue_S_button.pack(side="top")
        blue_O_button.pack(side="top")

        # creates computer option frames
        red_comp_frame = Frame(self.WIN)
        blue_comp_frame = Frame(self.WIN)

        # creates computer radio buttons for selecting which optino to use
        red_comp_button = Radiobutton(red_comp_frame, text='Computer', variable=self.game.red_type, value=constant.COMPUTER, command=lambda:self.game.set_red_computer(self.gameboard))
        blue_comp_button = Radiobutton(blue_comp_frame, text='Computer', variable=self.game.blue_type, value=constant.COMPUTER, command=lambda:self.game.set_blue_computer(self.gameboard))

        red_comp_frame.grid(row=3, column=self.BOARD_SIZE+2)
        blue_comp_frame.grid(row=3, column=self.BOARD_SIZE+3)
        red_comp_button.pack(side="top")
        blue_comp_button.pack(side="top")

        red_human_button.select()
        blue_human_button.select()
        red_S_button.select()
        blue_S_button.select()
            
if __name__ == '__main__':
    gameGUI = GAME_GUI()
    gameGUI.start()
