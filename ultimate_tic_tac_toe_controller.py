"""
Ultimate tic-tac-toe controller.
"""
from abc import ABC, abstractmethod

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
    def move(self):
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
                    print(self._ultimate_tic_tac_toe_board.current_move)
                    if sub_board.check_win(self._ultimate_tic_tac_toe_board.current_move):
                        self._ultimate_tic_tac_toe_board.mark_win(sub_board)
                    return mark_position
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
                        sub_board.won == False:
                    return sub_board_position
                raise ValueError
            except:
                print(f"{sub_board_position} was not a valid move.")


class GraphicalController(UltimateTicTacToeController):

    def move(self):
        pass
