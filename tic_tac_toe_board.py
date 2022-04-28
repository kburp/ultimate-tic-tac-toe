"""
Class representing a regular tic tac toe board.
"""


class TicTacToeBoard:

    current_move = "X"

    def __init__(self):
        self._board_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

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
        for index, row in enumerate(self._board_state):
            if row[0] == row[1] == row[2] == player:
                return True
            if self._board_state[0][index] == self._board_state[1][index] == \
                    self._board_state[2][index] == player:
                return True
        if self._board_state[0][0] == self._board_state[1][1] == \
            self._board_state[2][2] == player:
            return True
        return self._board_state[0][2] == self._board_state[1][1] == \
            self._board_state[2][0] == player

    @property
    def board_state(self):
        return self._board_state

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

