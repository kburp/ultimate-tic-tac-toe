"""
Class representing a regular tic tac toe board.
"""
import numpy as np


class TicTacToeBoard:

    current_move = "X"

    def __init__(self):
        self._board_state = np.array([
            [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def next_move(self):
        if self.current_move == "X":
            self.current_move = "O"
        else:
            self.current_move = "X"

    def mark(self, row, col):
        if self._board_state[row][col] == " ":
            self._board_state[row][col] = self.current_move
        else:
            raise ValueError

    def check_win(self, player):

        diag_win1 = self._board_state[0][0] == self._board_state[1][1] == self._board_state[2][2]
        diag_win2 = self._board_state[0][2] == self._board_state[1][1] == self._board_state[2][0]

        for i in range(0, 3):
            horizontal_win = np.all(self._board_state[i] == player)
            vertical_win = np.all(self._board_state[:, i] == player)

            if horizontal_win or vertical_win or diag_win1 or diag_win2:
                return True

        return False

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

