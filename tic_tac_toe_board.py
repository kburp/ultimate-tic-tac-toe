"""
Class representing a regular tic tac toe board.
"""


class TicTacToeBoard:
    """
    Tic-Tac-Toe board that will act as a sub board on the ultimate Tic-Tac-Toe
    board.
    """

    def __init__(self):
        """
        Creates an empty TicTacToeBoard.
        """
        self._board_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.move_count = 0
        self.win_state = 0

    @property
    def board_state(self):
        """
        Returns the value of _board_state
        """
        return self._board_state

    def mark(self, row, col, player):
        """
        Marks a given square on the Tic-Tac-Toe board with the current
        player's symbol. If there is already a symbol on that square,
        raise a ValueError.

        Args:
            row: An int representing the index of the row to be marked.
            col: An int representing the index of the column to be marked.
        """
        if self._board_state[row][col] == " ":
            self._board_state[row][col] = player
            self.move_count += 1
            if self.check_tie():
                self.win_state = 1
        else:
            raise ValueError

    def get_square(self, row, col):
        """
        Return the marked symbol of a given square.

        Args:
            row: An int representing the index of the row to be marked.
            col: An int representing the index of the column to be marked.

        Returns:
            The symbol which is on the given square ('X', 'O', or ' ').
        """
        return self.board_state[row][col]

    def check_tie(self):
        """
        Checks if the board is in a tied state.

        Returns:
            True if the board is in a tied state.
        """
        return self.move_count == 9

    def check_win(self, player):
        """
        Checks if the board is in a won state. Checks for horizontal, \
        vertical, and diagonal wins from the current player.

        Args:
            player: A string representing the player's symbol.

        Returns:
            True if the board is in a won state, False otherwise.
        """
        # Checks for horizontal and vertical wins
        for index, row in enumerate(self._board_state):
            if row[0] == row[1] == row[2] == player:
                return True
            if self._board_state[0][index] == self._board_state[1][index] == \
                    self._board_state[2][index] == player:
                return True

        # Checks for first diagonal win (left to right)
        if self._board_state[0][0] == self._board_state[1][1] == \
                self._board_state[2][2] == player:
            return True

        # Checks for second diagonal win (right to left)
        return self._board_state[0][2] == self._board_state[1][1] == \
            self._board_state[2][0] == player

    def __repr__(self):
        """
        Returns a string that represents the Tic-Tac-Toe Board (Not used only
        for testing
        """
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
