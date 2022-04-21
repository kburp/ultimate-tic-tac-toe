"""
Ultimate tic-tac-toe view.
"""
from abc import ABC, abstractmethod


class UltimateTicTacToeView(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class TextView(UltimateTicTacToeView):

    def draw(self):
        pass


class GraphicalView(UltimateTicTacToeView):

    def draw(self):
        pass
