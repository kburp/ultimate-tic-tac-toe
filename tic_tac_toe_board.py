"""
Class representing a regular tic tac toe board.
"""
import numpy as np


class TicTacToeBoard:

    def __init__(self):
        self._current_move = "X"
        self._board_state = np.array([
            [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def next_move(self):
        if self._current_move == "X":
            self._current_move = "O"
        else:
            self._current_move = "X"

    def mark(self, row, col):
        if self._board_state[row][col] == " ":
            self._board_state[row][col] = self._current_move
        else:
            raise ValueError

    def check_win(self, player):
        pass

    def __repr__(self):
        return "+-+-+-+\n" + \
            f"|{self._board_state[0][0]}|{self._board_state[0][1]}" + \
            f"|{self._board_state[0][2]}|\n" + \
            "+-+-+-+\n" + \
            f"|{self._board_state[1][0]}|{self._board_state[1][1]}" + \
            f"|{self._board_state[1][2]}|\n" + \
            "+-+-+-+\n" + \
            f"|{self._board_state[2][0]}|{self._board_state[2][1]}" + \
            f"|{self._board_state[2][2]}|\n" + \
            "+-+-+-+"


board = TicTacToeBoard()
print(board)
board.mark(0, 0)
print(board)
board.next_move()
board.mark(0, 1)
print(board)
