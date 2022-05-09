"""
Class representing an ultimate tic-tac-toe board.
"""
from tic_tac_toe_board import TicTacToeBoard


class UltimateTicTacToeBoard:
    """
    Represents an ultimate tic-tac-toe board.

    Attributes:
        boards: A list of lists containing instances of
            TicTacToeBoard objects that represent the
            3x3 grid of the board.
        _current_move: A string representing the marking
            symbol of the current player.
    """

    def __init__(self):
        """
        Creates an empty UltimateTicTacToeBoard.
        """
        self.boards = [[TicTacToeBoard() for i in range(3)] for j in range(3)]
        self._current_move = "X"

    def next_move(self):
        """
        Sets the current move to the player whose turn is next.
        """
        if self.current_move == "X":
            self._current_move = "O"
        else:
            self._current_move = "X"

    def mark_win(self, sub_board):
        """
        Marks a sub board with a special sequence of X or O to denote
        that that sub board has been won by a player.

        Args:
            sub_board: A TicTacToeBoard object to mark.
        """
        for subboard_row in range(0, 3):
            for subboard_column in range(0, 3):
                sub_board.board_state[subboard_row][subboard_column] = ' '
        if self.current_move == 'X':
            # mark the sub board in the shape of an X
            sub_board.board_state[0][0] = 'X'
            sub_board.board_state[0][2] = 'X'
            sub_board.board_state[1][1] = 'X'
            sub_board.board_state[2][0] = 'X'
            sub_board.board_state[2][2] = 'X'
            sub_board.win_state = 'X'
        else:
            # mark the sub board in the shape of an O
            sub_board.board_state[0][0] = 'O'
            sub_board.board_state[0][1] = 'O'
            sub_board.board_state[0][2] = 'O'
            sub_board.board_state[1][0] = 'O'
            sub_board.board_state[1][2] = 'O'
            sub_board.board_state[2][0] = 'O'
            sub_board.board_state[2][1] = 'O'
            sub_board.board_state[2][2] = 'O'
            sub_board.win_state = 'O'

    def get_board(self, row, col):
        """
        Given a row and column, returns the TicTacToeBoard at that index.

        Args:
            row: An int representing the row index on the
                UltimateTicTacToeBoard.
            col: An int representing the column index on the
                UltimateTicTacToeBoard.

        Returns:
            The TicTacToeBoard at the specified index.
        """
        return self.boards[row][col]

    @property
    def current_move(self):
        """
        Returns the private string _current_move.
        """
        return self._current_move

    def check_board_availability(self, sub_board):  # pylint: disable=no-self-use
        """
        Checks if a sub board of the UltimateTicTacToeBoard is available to
        play on.

        Args:
            sub_board: A TicTacToeBoard to check availability for.

        Returns:
            A boolean representing whether or not the TicTacToeBoard is
            available to play on.
        """
        if isinstance(sub_board.win_state, str) or sub_board.win_state == 1:
            return False
        return True

    def check_tie(self):
        """
        Checks if the game is tied or not.

        Returns:
            A boolean representing whether or not the game has ended in a tie.
        """
        for board_row in self.boards:
            for board in board_row:
                if board.win_state == 0:
                    return False
        return not self.check_win()

    def check_win(self):
        """
        Checks if a player has won the game.

        Returns:
            A string representing the marker of the player who has won the
            game. Returns False if neither player has won the game.
        """
        boards = self.boards
        for i in range(0, 3):
            # check horizontal win
            if boards[i][0].win_state == boards[i][1].win_state == \
                    boards[i][2].win_state and \
                    isinstance(boards[i][0].win_state, str):
                return boards[i][0].win_state
            # check vertical win
            if boards[0][i].win_state == boards[1][i].win_state == \
                    boards[2][i].win_state and \
                    isinstance(boards[0][i].win_state, str):
                return boards[0][i].win_state
        # check diagonal win
        if boards[0][0].win_state == boards[1][1].win_state == \
                boards[2][2].win_state and \
                isinstance(boards[1][1].win_state, str):
            return boards[0][0].win_state
        # check other diagonal win
        if boards[0][2].win_state == boards[1][1].win_state == \
                boards[2][0].win_state and \
                isinstance(boards[1][1].win_state, str):
            return boards[0][2].win_state
        return False

    def __repr__(self):
        """
        Returns an easily readable string representation of the board.
        """
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
