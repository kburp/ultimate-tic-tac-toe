"""
Ultimate tic-tac-toe controller.
"""
from abc import ABC, abstractmethod
from random import randint, shuffle

from matplotlib.style import available
from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard


class UltimateTicTacToeController(ABC):

    def __init__(self, UltimateTicTacToeBoard):
        self._ultimate_tic_tac_toe_board = UltimateTicTacToeBoard

    @property
    def board(self):
        """
        Return the value of _ticTacToeBoard attribute.
        """
        return self._ultimate_tic_tac_toe_board

    @abstractmethod
    def move(self, sub_board_position):
        pass


class TextController(UltimateTicTacToeController):

    def move(self, sub_board_position):
        sub_board = self._ultimate_tic_tac_toe_board.boards[sub_board_position[0]
                                                            ][sub_board_position[1]]
        while True:
            try:
                mark_position = input("Choose a row and a column (0 - 2): ")
                mark_position = [int(x) for x in mark_position.split()]
                if (0 <= mark_position[0] <= 2) and (0 <= mark_position[1] <= 2):
                    sub_board.mark(
                        mark_position[0], mark_position[1], self._ultimate_tic_tac_toe_board.current_move)
                    if sub_board.check_win(self._ultimate_tic_tac_toe_board.current_move):
                        self._ultimate_tic_tac_toe_board.mark_win(sub_board)
                    return mark_position, None
                else:
                    raise ValueError
            except:
                print(f"{mark_position} was not a valid move.")

    def choose_board(self):
        while True:
            try:
                sub_board_position = input(
                    "Choose the row and column of a board (0 - 2): ")
                sub_board_position = [int(x)
                                      for x in sub_board_position.split()]
                sub_board = self._ultimate_tic_tac_toe_board.boards[sub_board_position[0]
                                                                    ][sub_board_position[1]]
                if (0 <= sub_board_position[0] <= 2) and (0 <= sub_board_position[1] <= 2) and \
                        sub_board.win_state == 0:
                    return sub_board_position
                raise ValueError
            except:
                print(f"{sub_board_position} was not a valid move.")


class TextComputerController(UltimateTicTacToeController):

    def move(self, sub_board_position):
        """
        Given the coordinates of the opponent's last move, choose the
        computer's next move.

        Args:
            sub_board_position: A list of two integers representing
                the row and column within the TicTacToeBoard from the opponent's
                last move that also represent the row and column within the
                UltimateTicTacToeBoard that the computer will play on for
                the current turn.
        """
        sub_board = self._ultimate_tic_tac_toe_board.boards[sub_board_position[
            0]][sub_board_position[1]]
        while sub_board.win_state != 0:
            sub_board_position = (randint(0, 2), randint(0, 2))
            sub_board = self._ultimate_tic_tac_toe_board.boards[sub_board_position[0]
                                                                ][sub_board_position[1]]
        move_square = self.get_best_move(sub_board, self.board.current_move)
        sub_board.mark(move_square[0], move_square[1], self.board.current_move)
        if sub_board.check_win(self.board.current_move):
            self._ultimate_tic_tac_toe_board.mark_win(sub_board)
        return move_square, sub_board_position

    def get_best_move(self, sub_board, current_move):
        """
        Determines what the most strategic move for the computer is within
        the current TicTacToeBoard instance.

        After determinining which spaces are available, the best move is 
        determined in the following order: If there is only one space left
        on the board, take that space. If the board is empty, chose a random
        space. If there is an open space where the other two spaces in the row,
        column, or diagonal are both the current player's mark, chose that open
        space. Then, do the same thing but for the opposing player's mark. If
        there is an open space where the other two spaces in the row, column,
        or diagonal consist of one open space and one current player mark,
        chose that space. If none of these conditions apply, choose a random
        space.

        Args:
            sub_board: A TicTacToeBoard instance to get the best move for.
            current_move: A string representing the marker of the current
                player.
        """
        available_spaces = []
        for i in range(3):
            for j in range(3):
                if sub_board.get_square(i, j) == " ":
                    available_spaces.append([i, j])
        shuffle(available_spaces)
        if sub_board.move_count == 8 or sub_board.move_count == 0:
            return available_spaces[0]
        opponent_move = "X"
        if current_move == "X":
            opponent_move = "O"
        for space in available_spaces:
            if self.check_two_in_a_row(sub_board, space, current_move):
                return space
        for space in available_spaces:
            if self.check_two_in_a_row(sub_board, space, opponent_move):
                return space
        for space in available_spaces:
            if self.check_one_and_empty(sub_board, space, opponent_move):
                return space
        return available_spaces[0]

    def check_two_in_a_row(self, board, space, player):
        """
        Checks for a given empty square if the other two squares in the row or
        column (or diagonal) are filled by the same player marker.

        Args:
            board: A TicTacToeBoard to check conditions on.
            space: A list containing a row and column index for an empty space
                on the board.
            player: A string representing the player marker to check for two in
                a row.
        """
        row, col = space
        if board.get_square((row + 1) % 3, col) == \
                board.get_square((row + 2) % 3, col) == player:
            return True
        elif board.get_square(row, (col + 1) % 3) == \
                board.get_square(row, (col + 2) % 3) == player:
            return True
        if row + col == 2 and board.get_square((row + 1) % 3, (col - 1) % 3) \
                == board.get_square((row + 2) % 3, (col - 2) % 3) == player:
            return True
        return row == col and board.get_square((row + 1) % 3, (col + 1) % 3) \
            == board.get_square((row + 2) % 3, (col + 2) % 3) == player

    def check_one_and_empty(self, board, space, opponent):
        """
        Checks for a given empty square if the other two squares in the row or
        column (or diagonal) consist of one current player mark and one empty
        space.

        Args:
            board: A TicTacToeBoard to check conditions on.
            space: A list containing a row and column index for an empty space
                on the board.
            opponent: A string representing the marker of the opponent player.
        """
        row, col = space
        if board.get_square((row + 1) % 3, col) == \
                board.get_square((row + 2) % 3, col) or \
                board.get_square((row + 1) % 3, col) == opponent or \
                board.get_square((row + 2) % 3, col) == opponent:
            return False
        elif board.get_square(row, (col + 1) % 3) == \
                board.get_square(row, (col + 2) % 3) or \
                board.get_square(row, (col + 1) % 3) == opponent or \
                board.get_square(row, (col + 2) % 3) == opponent:
            return False
        elif row + col == 2 and \
            (board.get_square((row + 1) % 3, (col - 1) % 3) ==
             board.get_square((row + 2) % 3, (col - 2) % 3) or
             board.get_square((row + 1) % 3, (col - 1) % 3) == opponent or
             board.get_square((row + 2) % 3, (col - 2) % 3) == opponent):
            return False
        elif row == col and \
            (board.get_square((row + 1) % 3, (col + 1) % 3) ==
             board.get_square((row + 2) % 3, (col + 2) % 3) or
             board.get_square((row + 1) % 3, (col + 1) % 3) == opponent or
             board.get_square((row + 2) % 3, (col + 2) % 3) == opponent):
            return False
        return True


class GraphicalController(UltimateTicTacToeController):

    def move(self, sub_board_position, sub_board_square_position):
        sub_board = self._ultimate_tic_tac_toe_board.boards[sub_board_position[0]
                                                            ][sub_board_position[1]]
        try:
            if (0 <= sub_board_square_position[0] <= 2) and (0 <= sub_board_square_position[1] <= 2):
                sub_board.mark(
                    sub_board_square_position[0], sub_board_square_position[1], self._ultimate_tic_tac_toe_board.current_move)
                if sub_board.check_win(self._ultimate_tic_tac_toe_board.current_move):
                    self._ultimate_tic_tac_toe_board.mark_win(sub_board)
                return sub_board_square_position
            else:
                raise ValueError
        except:
            print(f"{sub_board_square_position} was not a valid move.")
            raise ValueError

    def choose_board(self, sub_board_position):
        try:
            sub_board = self._ultimate_tic_tac_toe_board.boards[sub_board_position[0]
                                                                ][sub_board_position[1]]
            if (0 <= sub_board_position[0] <= 2) and (0 <= sub_board_position[1] <= 2) and \
                    sub_board.win_state == 0:
                return sub_board_position
            raise ValueError
        except:
            print(f"{sub_board_position} was not a valid move.")
            raise ValueError
