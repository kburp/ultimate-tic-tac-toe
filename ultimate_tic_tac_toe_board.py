"""
Class representing an ultimate tic-tac-toe board.
"""

import numpy as np
from tic_tac_toe_board import TicTacToeBoard


class UltimateTicTacToeBoard:

    def __init__(self):
        self._boards = [[TicTacToeBoard() for i in range(3)] for j in range(3)]

    def __repr__(self):
        divider_string = "+-+-+-++-+-+-++-+-+-+\n"
        final_string = ""
        for i in range(3):
            for j in range(3):
                final_string += divider_string + "|"
                for k in range(3):
                    row = self._boards[i][k].board_state[j]
                    final_string += "|".join(row)
                    if k < 2:
                        final_string += "||"
                final_string += "|\n"
            final_string += divider_string
        return final_string
                    


uboard = UltimateTicTacToeBoard()
uboard._boards[1][2].mark(1, 1)
uboard._boards[1][2].mark(1, 2)
uboard._boards[1][2].mark(1, 0)
print(uboard)
