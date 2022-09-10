from tkinter import *

class SOS_GAME_BOARD():

    board = []
    ROWS = 6
    COLS = 6
    
    def __init__(self):
        self.create_board()

    def create_board(self): # makes a board of empty cells
        for row in range(self.ROWS):
            self.board.append([])
            for col in range(self.COLS):
                self.board[row].append(0)  

    def set_cell_value(self, row, col, value):
        self.board[row][col] = value

    def get_cell_value(self, row, col):
        return self.board[row][col]


class SOS_GAME_GUI():
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 1200
    WINDOW = Tk()
    WINDOW.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    WINDOW.title("Adam's SOS Game")
    PLAYER_OPTION =  StringVar()
    BUTTON_HEIGHT = 4
    BUTTON_WIDTH = 8

    def __init__(self):
        self.gameboard = SOS_GAME_BOARD()

    def start(self):
        self.create_GUI_board()
        self.WINDOW.mainloop() # places window on the computer screen

    def create_GUI_board(self):
        for r in range(self.gameboard.ROWS):
            for c in range(self.gameboard.COLS):
                self.gameboard.board[r][c] = Button(self.WINDOW, bg="SystemButtonFace", height=self.BUTTON_HEIGHT, width=self.BUTTON_WIDTH)
                self.gameboard.board[r][c].grid(row=r, column=c)
                
        player_text = Label(self.WINDOW, text='PLAYER 1')
        player_text.grid(row=1, column=7)

        S_button = Radiobutton(self.WINDOW, text='S', variable= self.PLAYER_OPTION, value='S').grid(row=2, column=7)
        O_checkbox = Checkbutton(self.WINDOW, text='O', variable= self.PLAYER_OPTION, onvalue=1, offvalue=0).grid(row=3, column=7)



# MAIN
game = SOS_GAME_GUI()
game.start()
