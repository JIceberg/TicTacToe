from tkinter import *
from enum import Enum
import numpy as np  # the lord and savior

class Tile(Enum):
    TOP_LEFT = (0, 0)
    TOP_MID = (0, 1)
    TOP_RIGHT = (0, 2)
    MID_LEFT = (1, 0)
    MID_MID = (1, 1)
    MID_RIGHT = (1, 2)
    BOTTOM_LEFT = (2, 0)
    BOTTOM_MID = (2, 1)
    BOTTOM_RIGHT = (2, 2)

'''
Uses the backing board

@return a string representing the player (X or O) who has won the game
        if no one has won, returns an empty string
'''
def detect_win(board) -> str:
    # check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]
    # check columns
    # it's a square... but should obv be refactored to be more pleasing
    for col in range(len(board[0])):
        curr_col = np.array(board)[:,col]
        if len(set(curr_col)) == 1 and curr_col[0] != '':
            return curr_col[0]
        
    # check diagonals
    tmp_arr = np.array(board)   # let's use this one object for our diags
    main_diag = tmp_arr.diagonal()
    other_diag = np.flipud(tmp_arr).diagonal()  # eggmega 🥚

    if len(set(main_diag)) == 1 and main_diag[0] != '':
        return main_diag[0]
    elif len(set(other_diag)) == 1 and other_diag[0] != '':
        return other_diag[0]

    return ''

'''
@TODO: Gonna make this actually nice in the future; for now,
       core functionality just changes the text label in the button
'''
def run(tile: Tile, turn, board, button: Button) -> None:
    if board[tile.value[0]][tile.value[1]] != '': return
    elif (winner := detect_win(board)) != '':
        print("{} has won!".format(winner)) # garbage temp stdout for detecting winner
        return
    board[tile.value[0]][tile.value[1]] = 'O' if not turn[0] else 'X'
    print(board)    # for debugging the backing board
    button['text'] = '0' if not turn[0] else 'X'
    turn[0] = not turn[0]   # scuffed way of making this update the boolean

turn = [True]    # player turn
board = [['' for i in range(3)] for i in range(3)]  # store board positions

tk = Tk()
tk.title("Tic-Tac-Toe")

# god this is ugly
'''
#FIXME: This is bastardization of a fairly nice language
'''
main = Frame(tk)
main.pack(side = TOP)
e_00 = Button(main, width=24, height=12, command=lambda: run(Tile.TOP_LEFT, turn, board, e_00))
e_00.grid(row=0, column=0)
e_01 = Button(main, width=24, height=12, command=lambda: run(Tile.TOP_MID, turn, board, e_01))
e_01.grid(row=0, column=1)
e_02 = Button(main, width=24, height=12, command=lambda: run(Tile.TOP_RIGHT, turn, board, e_02))
e_02.grid(row=0, column=2)
e_10 = Button(main, width=24, height=12, command=lambda: run(Tile.MID_LEFT, turn, board, e_10))
e_10.grid(row=1, column=0)
e_11 = Button(main, width=24, height=12, command=lambda: run(Tile.MID_MID, turn, board, e_11))
e_11.grid(row=1, column=1)
e_12 = Button(main, width=24, height=12, command=lambda: run(Tile.MID_RIGHT, turn, board, e_12))
e_12.grid(row=1, column=2)
e_20 = Button(main, width=24, height=12, command=lambda: run(Tile.BOTTOM_LEFT, turn, board, e_20))
e_20.grid(row=2, column=0)
e_21 = Button(main, width=24, height=12, command=lambda: run(Tile.BOTTOM_MID, turn, board, e_21))
e_21.grid(row=2, column=1)
e_22 = Button(main, width=24, height=12, command=lambda: run(Tile.BOTTOM_RIGHT, turn, board, e_22))
e_22.grid(row=2, column=2)

tk.mainloop()
