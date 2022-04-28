"""
Class representing an ultimate tic-tac-toe board.
"""

import numpy as np
from tic_tac_toe_board import TicTacToeBoard


class UltimateTicTacToeBoard:

    def __init__(self):
        self._boards = []
        self._ultimate_board_state = []
        for i in range(0, 9):
            self._boards.append(TicTacToeBoard())
            self._ultimate_board_state.append(self._boards[i])

    def __repr__(self):
        ultimate_board_string = ""
        for board_count in range(0, 3):
            boards = self._ultimate_board_state[(
                board_count*3): (3 + board_count*3)]
            big_row_str = ""
            for row_count in range(0, 3):
                row_str = str(boards[:][row_count]) + "\n"
                big_row_str += row_str

            ultimate_board_string += big_row_str
        return (ultimate_board_string)


uboard = UltimateTicTacToeBoard()
uboard._ultimate_board_state[0].mark(1, 1)
print(uboard)
