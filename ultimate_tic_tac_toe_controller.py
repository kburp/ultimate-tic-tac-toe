"""
Ultimate tic-tac-toe controller.
"""
from abc import ABC, abstractmethod

from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard


class UltimateTicTacToeController(ABC):

    def __init__(self):
        self._ultimate_tic_tac_toe_board = UltimateTicTacToeBoard

    @property
    def board(self):
        """
        Return the value of _ticTacToeBoard attribute.
        """
        return self._ultimate_tic_tac_toe_board

    @abstractmethod
    def move(self):
        pass


class TextController(UltimateTicTacToeController):

    def move(self):
        if _ultimate first_move == true:


class GraphicalController(UltimateTicTacToeController):

    def move(self):
        pass


tc = TextController()
tc.move()
