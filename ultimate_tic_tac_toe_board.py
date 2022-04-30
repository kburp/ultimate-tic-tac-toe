"""
Class representing an ultimate tic-tac-toe board.
"""

import numpy as np
from tic_tac_toe_board import TicTacToeBoard


class UltimateTicTacToeBoard:

    def __init__(self):
        self.boards = [[TicTacToeBoard() for i in range(3)] for j in range(3)]
        self.current_move = "X"

    def next_move(self):
        if self.current_move == "X":
            self.current_move = "O"
        else:
            self.current_move = "X"

    def mark_win(self, sub_board):
        for subboard_row in range(0, 3):
            for subboard_column in range(0, 3):
                sub_board.board_state[subboard_row][subboard_column] = ' '
        if self.current_move == 'X':
            sub_board.board_state[0][0] = 'X'
            sub_board.board_state[0][2] = 'X'
            sub_board.board_state[1][1] = 'X'
            sub_board.board_state[2][0] = 'X'
            sub_board.board_state[2][2] = 'X'
            sub_board.won = True
        else:
            sub_board.board_state[0][0] = 'O'
            sub_board.board_state[0][1] = 'O'
            sub_board.board_state[0][2] = 'O'
            sub_board.board_state[1][0] = 'O'
            sub_board.board_state[1][2] = 'O'
            sub_board.board_state[2][0] = 'O'
            sub_board.board_state[2][1] = 'O'
            sub_board.board_state[2][2] = 'O'
            sub_board.won = True

    def check_win(self):
        boards = self.boards
        for i in range(0, 3):
            if boards[i][0].won == boards[i][1].won == boards[i][2].won == True:
                return True
            if boards[0][i].won == boards[1][i].won == boards[2][i].won == True:
                return True
        if boards[0][0].won == boards[1][1].won == boards[2][2].won == True:
            return True
        if boards[0][2].won == boards[1][1].won == boards[2][0].won == True:
            return True
        return False

    def __repr__(self):
        divider_string = "+-+-+-++-+-+-++-+-+-+\n"
        final_string = ""
        for i in range(3):
            for j in range(3):
                final_string += divider_string + "|"
                for k in range(3):
                    row = self.boards[i][k].board_state[j]
                    final_string += "|".join(row)
                    if k < 2:
                        final_string += "||"
                final_string += "|\n"
            final_string += divider_string
        return final_string
