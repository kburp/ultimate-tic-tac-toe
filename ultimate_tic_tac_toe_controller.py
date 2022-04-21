"""
Ultimate tic-tac-toe controller.
"""
from abc import ABC, abstractmethod


class UltimateTicTacToeController(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def move(self):
        pass


class TextController(UltimateTicTacToeController):

    def move(self):
        pass


class GraphicalController(UltimateTicTacToeController):

    def move(self):
        pass
