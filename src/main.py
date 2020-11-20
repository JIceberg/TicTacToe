from tkinter import *
from enum import Enum

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

def run(tile: Tile, turn, board) -> None:
    if board[tile.value[0]][tile.value[1]] != '': return
    board[tile.value[0]][tile.value[1]] = 'O' if not turn[0] else 'X'
    turn[0] = not turn[0]   # scuffed way of making this update the boolean

turn = [True]    # player turn
board = [['' for i in range(3)] for i in range(3)]  # store board positions

tk = Tk()
tk.title("Tic-Tac-Toe")

main = Frame(tk)
main.pack(side = TOP)
e_00 = Button(main, width=24, height=12, command=lambda: run(Tile.TOP_LEFT, turn, board))
e_00.grid(row=0, column=0)
e_01 = Button(main, width=24, height=12, command=lambda: run(Tile.TOP_MID, turn, board))
e_01.grid(row=0, column=1)
e_02 = Button(main, width=24, height=12, command=lambda: run(Tile.TOP_RIGHT, turn, board))
e_02.grid(row=0, column=2)
e_10 = Button(main, width=24, height=12, command=lambda: run(Tile.MID_LEFT, turn, board))
e_10.grid(row=1, column=0)
e_11 = Button(main, width=24, height=12, command=lambda: run(Tile.MID_MID, turn, board))
e_11.grid(row=1, column=1)
e_12 = Button(main, width=24, height=12, command=lambda: run(Tile.MID_RIGHT, turn, board))
e_12.grid(row=1, column=2)
e_20 = Button(main, width=24, height=12, command=lambda: run(Tile.BOTTOM_LEFT, turn, board))
e_20.grid(row=2, column=0)
e_21 = Button(main, width=24, height=12, command=lambda: run(Tile.BOTTOM_MID, turn, board))
e_21.grid(row=2, column=1)
e_22 = Button(main, width=24, height=12, command=lambda: run(Tile.BOTTOM_RIGHT, turn, board))
e_22.grid(row=2, column=2)

tk.mainloop()
