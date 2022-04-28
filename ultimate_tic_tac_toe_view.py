"""
Ultimate tic-tac-toe view.
"""
from abc import ABC, abstractmethod


class UltimateTicTacToeView(ABC):

    def __init__(self, board):
        self._board = board

    @property
    def board(self):
        return self._board

    @abstractmethod
    def draw(self):
        pass


class TextView(UltimateTicTacToeView):

    def draw(self):
        print(self.board)


class GraphicalView(UltimateTicTacToeView):

    def draw(self):
        pass
