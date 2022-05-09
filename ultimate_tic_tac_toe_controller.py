"""
Ultimate tic-tac-toe controller.
"""
from abc import ABC, abstractmethod
from random import randint, shuffle


class UltimateTicTacToeController(ABC):
    """
    An abstract class that provides decorator properties and abstract mehods
    for multiple controller sub classes.

    Attributes:
        _ultimate_tic_tac_toe_board: An UltimateTicTacToeBoard object.
        board: A decorator property that returns
            self._ultimate_tic_tac_toe_board.
    """

    def __init__(self, UltimateTicTacToeBoard):  # pylint: disable=redefined-outer-name
        self._ultimate_tic_tac_toe_board = UltimateTicTacToeBoard

    @property
    def board(self):
        """
        Return the value of _ultimate_tic_tac_toe_board attribute.
        """
        return self._ultimate_tic_tac_toe_board

    @abstractmethod
    def move(self, sub_board_position):
        """
        An abstract method for getting the players move on a given
        sub board.
        """


class TextController(UltimateTicTacToeController):
    """
    A subclass of TicTacToeController that provides functionallity for
    player input textually through the terminal.
    """

    def move(self, sub_board_position):
        """
        Asks for the square that the player wants to chose on a given sub
        board. Handles incorrect input with exceptions and reasks for valid
        input until a valid move is inputted.

        Args:
            sub_board_position: A tuple of two integers which represent the
                index of the row of the sub board and index of the column of
                the sub board within the larger ultimate tic-tac-toe-board.

        Returns:
            A tuple containing two items:
                A tuple containing two integers representing the index
                of the row and column of the square chosen on a sub board.
                The value None, which is a helper value for the main game
                function.
        """
        sub_board = self._ultimate_tic_tac_toe_board.boards[
            sub_board_position[0]][sub_board_position[1]]
        while True:
            try:
                # Ask for input
                mark_position = input("Choose a row and a column (0 - 2): ")
                mark_position = [int(x) for x in mark_position.split()]

                # Check if input is valid
                if (0 <= mark_position[0] <= 2) and \
                        (0 <= mark_position[1] <= 2):
                    sub_board.mark(
                        mark_position[0], mark_position[1],
                        self._ultimate_tic_tac_toe_board.current_move)

                    # Check for a win condition
                    if sub_board.check_win(self._ultimate_tic_tac_toe_board.
                                           current_move):
                        self._ultimate_tic_tac_toe_board.mark_win(sub_board)
                    return mark_position, None
                raise ValueError
            except ValueError:
                print(f"{mark_position} was not a valid move.")

    def choose_board(self):
        """
        Asks for the row and column of the sub board that the player wants
        to select. Called when the first player must choose the starting
        board and when a player must chose a new valid board.

        Returns:
            A tuple containing two integers representing the index
            of the row and column of the sub board within the
            ultimate tic-tac-toe board.
        """
        while True:
            try:
                # Ask for input
                sub_board_position = input(
                    "Choose the row and column of a board (0 - 2): ")
                sub_board_position = [int(x)
                                      for x in sub_board_position.split()]
                sub_board = self._ultimate_tic_tac_toe_board.boards[
                    sub_board_position[0]][sub_board_position[1]]
                # Check if input is valid and win condition
                if (0 <= sub_board_position[0] <= 2) and \
                    (0 <= sub_board_position[1] <= 2) and \
                        sub_board.win_state == 0:
                    return sub_board_position
                raise ValueError
            except ValueError:
                print(f"{sub_board_position} was not a valid move.")


class TextComputerController(UltimateTicTacToeController):
    """
    A subclass of TicTacToeController that provides functionallity for
    AI input (works for text and graphical views).
    """

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

        Returns:
            A list of two ints representing the row and column index of a space
            within a TicTacToeBoard and a tuple of two ints representing the
            row and column index of a TicTacToeBoard within the
            UltimateTicTacToeBoard.
        """
        sub_board = self._ultimate_tic_tac_toe_board.boards[sub_board_position[
            0]][sub_board_position[1]]
        while sub_board.win_state != 0:
            sub_board_position = (randint(0, 2), randint(0, 2))
            sub_board = self._ultimate_tic_tac_toe_board.boards[
                sub_board_position[0]][sub_board_position[1]]
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

        Returns:
            A list of two integers representing the row and column index of a
            TicTacToeBoard.
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

    def check_two_in_a_row(self, board, space, player):  # pylint: disable=no-self-use
        """
        Checks for a given empty square if the other two squares in the row or
        column (or diagonal) are filled by the same player marker.

        Args:
            board: A TicTacToeBoard to check conditions on.
            space: A list containing a row and column index for an empty space
                on the board.
            player: A string representing the player marker to check for two in
                a row.

        Returns:
            A boolean representing whether or not the condition described above
            has been met.
        """
        row, col = space
        if board.get_square((row + 1) % 3, col) == \
                board.get_square((row + 2) % 3, col) == player:
            return True
        if board.get_square(row, (col + 1) % 3) == \
                board.get_square(row, (col + 2) % 3) == player:
            return True
        if row + col == 2 and board.get_square((row + 1) % 3, (col - 1) % 3) \
                == board.get_square((row + 2) % 3, (col - 2) % 3) == player:
            return True
        return row == col and board.get_square((row + 1) % 3, (col + 1) % 3) \
            == board.get_square((row + 2) % 3, (col + 2) % 3) == player

    def check_one_and_empty(self, board, space, opponent):  # pylint: disable=no-self-use
        """
        Checks for a given empty square if the other two squares in the row or
        column (or diagonal) consist of one current player mark and one empty
        space.

        Args:
            board: A TicTacToeBoard to check conditions on.
            space: A list containing a row and column index for an empty space
                on the board.
            opponent: A string representing the marker of the opponent player.

        Returns:
            A boolean representing whether or not the condition described above
            has been met.
        """
        row, col = space
        if board.get_square((row + 1) % 3, col) == \
                board.get_square((row + 2) % 3, col) or \
                board.get_square((row + 1) % 3, col) == opponent or \
                board.get_square((row + 2) % 3, col) == opponent:
            return False
        if board.get_square(row, (col + 1) % 3) == \
                board.get_square(row, (col + 2) % 3) or \
                board.get_square(row, (col + 1) % 3) == opponent or \
                board.get_square(row, (col + 2) % 3) == opponent:
            return False
        if row + col == 2 and \
            (board.get_square((row + 1) % 3, (col - 1) % 3) ==
             board.get_square((row + 2) % 3, (col - 2) % 3) or
             board.get_square((row + 1) % 3, (col - 1) % 3) == opponent or
             board.get_square((row + 2) % 3, (col - 2) % 3) == opponent):
            return False
        if row == col and \
            (board.get_square((row + 1) % 3, (col + 1) % 3) ==
             board.get_square((row + 2) % 3, (col + 2) % 3) or
             board.get_square((row + 1) % 3, (col + 1) % 3) == opponent or
             board.get_square((row + 2) % 3, (col + 2) % 3) == opponent):
            return False
        return True


class GraphicalController(UltimateTicTacToeController):
    """
    A subclass of TicTacToeController that provides functionallity for
    player input graphically through a pygame window.
    """

    def move(self, sub_board_position, sub_board_square_position):  # pylint: disable=arguments-differ
        """
        Asks for the square that the player wants to chose on a given sub
        board. Handles incorrect input with exceptions and reasks for valid
        input until a valid move is inputted.

        Args:
            sub_board_position: A tuple of two integers which represent the
                index of the row of the sub board and index of the column of
                the sub board within the larger ultimate tic-tac-toe-board.
            sub_board_square_position: A tuple of two integers which represent
                the row and column of the selected square within the sub board.

        Returns:
            A tuple containing two items:
                A tuple containing two integers representing the index
                of the row and column of the square chosen on a sub board.
                The value None, which is a helper value for the main game
                function.
        """
        sub_board = self._ultimate_tic_tac_toe_board.boards[
            sub_board_position[0]][sub_board_position[1]]
        try:
            if (0 <= sub_board_square_position[0] <= 2) and \
                    (0 <= sub_board_square_position[1] <= 2):
                sub_board.mark(
                    sub_board_square_position[0],
                    sub_board_square_position[1],
                    self._ultimate_tic_tac_toe_board.current_move)
                if sub_board.check_win(
                        self._ultimate_tic_tac_toe_board.current_move):
                    self._ultimate_tic_tac_toe_board.mark_win(sub_board)
                return sub_board_square_position
            raise ValueError
        except ValueError as v_err:
            raise ValueError from v_err

    def choose_board(self, sub_board_position):
        """
        Asks for the row and column of the sub board that the player wants
        to select. Called when the first player must choose the starting
        board and when a player must chose a new valid board.

        Returns:
            A tuple containing two integers representing the index
            of the row and column of the sub board within the
            ultimate tic-tac-toe board.
        """
        try:
            sub_board = self._ultimate_tic_tac_toe_board.boards[
                sub_board_position[0]][sub_board_position[1]]
            if (0 <= sub_board_position[0] <= 2) and \
                (0 <= sub_board_position[1] <= 2) and \
                    sub_board.win_state == 0:
                return sub_board_position
            raise ValueError
        except ValueError as v_err:
            raise ValueError from v_err
