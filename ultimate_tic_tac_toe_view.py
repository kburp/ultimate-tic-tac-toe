"""
Ultimate tic-tac-toe view.
"""
from abc import ABC, abstractmethod


class UltimateTicTacToeView(ABC):
    """
    ABC for the game view.

    Attributes:
        _board: An UltimateTicTacToeBoard instance.
    """

    def __init__(self, board):
        self._board = board

    @property
    def board(self):
        """
        Returns the private UltimateTicTacToeBoard _board.
        """
        return self._board

    @abstractmethod
    def draw(self, sub_board_position):
        """
        Abstract method for drawing for the view class.
        """


class TextView(UltimateTicTacToeView):
    """
    Game view for the text version of the game.
    """

    def draw(self, sub_board_position):
        """
        Prints whose turn it is, the current state of the board, and which
        board to move on next.
        """
        print(self.board)
        print(f"It is now {self.board.current_move}'s turn.")
        if self.board.get_board(sub_board_position[0],
                                sub_board_position[1]).win_state == 0:
            print(f"Playing on board {sub_board_position}.")
