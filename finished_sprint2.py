from tkinter import *
from tkinter import messagebox

class GAME_BOARD():
    # class used for creating the game board based on chosen board size

    def __init__(self, board_size):
        self.row_num = board_size
        self.col_num = board_size
        self.board = []
        self.create_skeleton()
        
    def create_skeleton(self):
        # creates empty board
        for row in range(self.row_num):
            self.board.append([])
            for col in range(self.col_num):
                self.board[row].append(0)  # append empty cell
                
    def cell_button(self, row, col):
        # used for accessing a cell given a row and column number
        return self.board[row][col]
                
    def reset_board(self):
        # returns board to initial state
        for r in range(self.row_num):
            for c in range(self.col_num):
                tile = self.board[r][c]
                tile['text'] = ' '
                tile['bg'] = 'white'
                
    def full_board_check(self):
        # used to check if the board is full
        for row in range(self.row_num):
            for col in range(self.col_num):
                if self.board[row][col]['text'] == ' ':
                    return False
        return True

class Player():
    # class used for each player
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.option = StringVar()
        
    def get_option(self):
        # used to check if player has selected 'S' or 'O'
        return self.option
   
class GAME_GUI(GAME_BOARD):
    # class used for the SOS game's GUI
    
    def __init__(self, board_size):
        super().__init__(board_size)
        self.WIN = Tk()
        self.WIN_WIDTH = 1200
        self.WIN_HEIGHT = 700
        self.WIN_TITLE = 'SOS'
        self.BUTTON_HEIGHT = 4
        self.BUTTON_WIDTH = 8
        self.R_TURN = 'Red Player\'s Turn'
        self.B_TURN = 'Blue Player\'s Turn'
        self.SIMPLE_GAME = 'Simple Game'
        self.GENERAL_GAME = 'General Game'
        self.red_player = Player("red player", "red")
        self.blue_player = Player("blue player", "blue")
        self.current_turn = StringVar()
        self.gametype = ' '
        self.set_r_turn()
        
    def start(self):
        # displays window
        self.WIN.mainloop()
            
    def restart(self):
        # used for restarting the game if restart button is hit
        self.reset_board()
        self.set_r_turn()
        
    def is_simple(self):
        # checks if the gametype is a simple game
        return self.gametype == self.SIMPLE_GAME
        
    def is_general(self):
        # checks if the gametype is a general game
        return self.gametype == self.GENERAL_GAME
        
    def start_simple(self):
        # sets the gametype to "simple game"
        self.gametype = self.SIMPLE_GAME
        messagebox.showinfo('Gametype', self.gametype)
        
    def start_general(self):
        # sets the gametype to "general game"
        self.gametype = self.GENERAL_GAME
        messagebox.showinfo('Gametype', self.gametype)
        
    def gameboard_GUI(self):
        # creates the GUI for the gameboard
        self.WIN.geometry(f"{self.WIN_WIDTH}x{self.WIN_HEIGHT}")
        self.WIN.title(self.WIN_TITLE)
        
        # creates the buttons that fill up the gameboard
        for r in range(self.row_num):
            for c in range(self.col_num):
                tile = self.board[r][c] = Button(
                    self.WIN, bg="white", text=' ', height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH, command=lambda row1=r, col1=c: self.move(row1, col1))
                tile.grid(row=r, column=c, padx=2, pady=2)
                
        # creates the gametype buttons
        simple_game_button = Radiobutton(self.WIN, text='Simple Game', variable=self.gametype,
                                         value=self.SIMPLE_GAME, command=lambda: self.start_simple())
        simple_game_button.grid(row=0, column=self.col_num+2)
        general_game_button = Radiobutton(self.WIN, text='General Game', variable=self.gametype,
                                          value=self.GENERAL_GAME, command=lambda: self.start_general())
        general_game_button.grid(row=0, column=self.col_num+3)
        
        # creates restart button
        restart_game_button = Button(
            self.WIN, text='Restart Game', command=lambda: self.restart())
        restart_game_button.grid(row=5, column=self.col_num+3)
        
        # creates the player labels
        red_label = Label(self.WIN, text='Red Player')
        red_label.grid(row=1, column=self.col_num+2)
        blue_label = Label(self.WIN, text='Blue Player')
        blue_label.grid(row=1, column=self.col_num+3, padx=100)
        
        # creates the 'S' and 'O' buttons for both players
        red_S_button = Radiobutton(
            self.WIN, text='S', variable=self.red_player.option, value='S')
        red_S_button.grid(row=2, column=self.col_num+2)
        red_O_button = Radiobutton(
            self.WIN, text='O', variable=self.red_player.option, value='O')
        red_O_button.grid(row=3, column=self.col_num+2)
        blue_S_button = Radiobutton(
            self.WIN, text='S', variable=self.blue_player.option, value='S')
        blue_S_button.grid(row=2, column=self.col_num+3)
        blue_O_button = Radiobutton(
            self.WIN, text='O', variable=self.blue_player.option, value='O')
        blue_O_button.grid(row=3, column=self.col_num+3)
        
        # displays whose turn it is currently
        current_turn_text = Label(self.WIN, textvariable=self.current_turn)
        current_turn_text.grid(row=5, column=self.col_num+1)
        
    def move(self, row, col):
        # used for making a move in one of the cells
        tile = self.cell_button(row, col)
        
        if self.gametype == ' ':
            # error displayed if no gametype was chosen and a player tries to make a move
            messagebox.showerror('No Gamemode Selected', 'Select a gamemode to begin.')
            
        elif tile['text'] == 'S' or tile['text'] == 'O':
            # error displayed if player tries to make a turn on an occupied cell
            messagebox.showerror(
                'Invalid Move', 'This cell is already occupied. Select an empty cell.')
            
        elif (self.get_current_turn() == self.R_TURN):
            # these are checks that are done if it's the red player's turn
            if self.red_player.option.get() != 'S' and self.red_player.option.get() != 'O':
                # error displayed if player didn't select an option before attempting to make a move
                messagebox.showerror('No Letter Selected', 'You must chose either \'S\' or \'O\' in order to place a letter on the board.')
                return None
            tile['text'] = self.red_player.option.get()
            color = self.red_player.color

            if self.is_simple():
                # checks if board is full in a simple game. If full, the game restarts. If not, it's now the blue player's turn
                if self.full_board_check():
                    self.restart()
                    return None
                else:
                    self.set_b_turn()

            elif self.is_general():
                # checks if board is full in a general game. If full, the game restarts. If not, it's now the blue player's turn
                if self.full_board_check():
                    self.restart()
                    return None
                else:
                    self.set_b_turn()
                    
        elif (self.get_current_turn() == self.B_TURN):
            # these are checks that are done if it's the blue player's turn
            if self.blue_player.option.get() != 'S' and self.blue_player.option.get() != 'O':
                # error displayed if player didn't select an option before attempting to make a move
                messagebox.showerror('No Letter Selected', 'You must chose either \'S\' or \'O\' in order to place a letter on the board.')
                return None
            tile['text'] = self.blue_player.option.get()
            color = self.blue_player.color

            if self.is_simple():
                # checks if board is full in a simple game. If full, the game restarts. If not, it's now the red player's turn
                if self.full_board_check():
                    self.restart()
                    return None
                else:
                    self.set_r_turn()

            if self.is_general():
                # checks if board is full in a general game. If full, the game restarts. If not, it's now the red player's turn
                if self.full_board_check():
                    if self.full_board_check():
                        self.restart()
                    return None
                else:
                    self.set_r_turn()
                        
    def set_r_turn(self):
        # makes it the red player's turn
        self.current_turn.set(self.R_TURN)
        
    def set_b_turn(self):
        # makes it the blue player's turn
        self.current_turn.set(self.B_TURN)
                        
    def get_current_turn(self):
        # returns whose turn it is
        return self.current_turn.get()
        
class START_MENU():
    # class used for the start menu that displays when the file is run. The start menu is used for selecting the board size before the SOS game itself is displayed
    
    def __init__(self):
        self.WIN_SIZE = Tk()
        self.WIN_SIZE.geometry("400x200")
        self.WIN_SIZE.title("Choose the Board Size")
        self.record = BooleanVar()
        self.label = Label(self.WIN_SIZE, text="Enter the board size (must be greater than 2)")
        self.label.pack()
        self.enter_size = Entry(self.WIN_SIZE)
        self.enter_size.pack()
        self.start_button = Button(self.WIN_SIZE, height=4, width=10, text="START", command=lambda:self.start_game())
        self.start_button.pack()
        
    def display_menu(self):
        # displays the menu
        self.WIN_SIZE.mainloop()
        
    def start_game(self):
        # starts the game using given board size
        try:
            board_size = self.enter_size.get()
            board_size = int(board_size)
        except ValueError:
            # error is displayed if the value entered isn't an integer
            messagebox.showerror(
                'Invalid Board Size', 'The board size must be an integer.')
            return None
            
        if board_size < 3:
            # error is displayed if the value entered is too small
            messagebox.showerror(
                'Invalid Board Size', 'The board size must be greater than 2.')
            return None
        else:
            # The start menu is closed and the gameboard GUI is created
            self.WIN_SIZE.destroy()
            game = GAME_GUI(board_size)
            game.gameboard_GUI()
            game.start()
            
if __name__ == '__main__':
    # the start menu is displayed when the program is run
    start = START_MENU()
    start.display_menu()
