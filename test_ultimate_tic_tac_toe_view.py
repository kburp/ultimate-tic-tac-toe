"""
Unit tests for ultimate tic tac toe view.
"""
import pytest
from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard
from ultimate_tic_tac_toe_view import TextView


@pytest.fixture()
def board():
    """
    Create an ultimate tic tac toe board for use in testing.
    """
    return UltimateTicTacToeBoard()


# add cases to this list
board_reprs = [
    ([(1, 1, 1, 1)],    "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || | | || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || | | || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || | | || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || | | || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || |X| || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || | | || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || | | || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || | | || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n"
                        "| | | || | | || | | |\n"
                        "+-+-+-++-+-+-++-+-+-+\n\n"
                        "It is now O's turn.\n"
                        "Playing on board [1, 1]."),
    ([(2, 2, 1, 0), (1, 0, 1, 1), (1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 1, 1), \
        (1, 1, 2, 2), (2, 2, 2, 0), (2, 0, 1, 0), (1, 0, 1, 0), (1, 0, 2, 1), \
            (2, 1, 0, 2), (0, 2, 0, 0)],    "+-+-+-++-+-+-++-+-+-+\n"
                                            "| | | || | | ||O| | |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "| | | || | | || | | |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "| | | || | | || | | |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "| | | || | | || | | |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "|X|O| || |X|O|| |X| |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "| |O| || | |O|| | | |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "| | | || | |X|| | | |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "|O| | || | | ||X| | |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n"
                                            "| | | || | | ||X| | |\n"
                                            "+-+-+-++-+-+-++-+-+-+\n\n"
                                            "It is now X's turn.\n"
                                            "Playing on board [0, 0]."),
([(0, 0, 0, 0), (0, 0, 1, 1), (1, 1, 1, 2), (1, 2, 2, 0), (2, 0, 1, 1), \
    (1, 1, 1, 1), (1, 1, 2, 2), (2, 2, 2, 1), (2, 1, 1, 0), (1, 0, 1, 0), \
    (1, 0, 2, 1), (2, 1, 1, 2), (1, 2, 2, 2), (2, 2, 2, 2), (2, 2, 0, 2), \
    (0, 2, 1, 0), (1, 0, 0, 1), (0, 1, 2, 0), (2, 0, 0, 1), (0, 1, 1, 1), \
    (1, 1, 3, 3), (0, 2, 2, 0)],    "+-+-+-++-+-+-++-+-+-+\n"
                                    "|X| | || | | || | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| |O| || |O| ||O| | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | ||O| | ||O| | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| |X| ||X| |X|| | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "|O| | || |X| || | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| |X| ||X| |X||O| |X|\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| |X| || | | || | |X|\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| |X| ||X| |O|| | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | || | | || |O|O|\n"
                                    "+-+-+-++-+-+-++-+-+-+\n\n"
                                    "It is now X's turn.\n"
                                    "Playing on board [2, 0]."),
([(1, 1, 1, 1), (1, 1, 2, 2), (2, 2, 1, 1), (1, 1, 2, 1), (2, 1, 1, 1), \
    (1, 1, 3, 3), (2, 0, 1, 1)],    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | || | | || | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | || | | || | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | || | | || | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | ||O|O|O|| | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | ||O| |O|| | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | ||O|O|O|| | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | || | | || | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| |X| || |X| || |X| |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n"
                                    "| | | || | | || | | |\n"
                                    "+-+-+-++-+-+-++-+-+-+\n\n"
                                    "It is now O's turn."),
]

@pytest.fixture(params=board_reprs)
def game_repr(request):
    """
    Create a representation of a sequence of moves for use in testing.
    """
    return request.param


def test_draw(board, game_repr, capsys): # pylint: disable=redefined-outer-name
    """
    Test that the draw function is working as intended.

    Args:
        board: The UltimateTicTacToeBoard instance to use
        game_repr:
    """
    moves, board_repr = game_repr
    for board_row, board_column, row, col in moves: # pylint: disable=redefined-outer-name
        sub_board = board.get_board(board_row, board_column)
        if row == col == 3:
            board.mark_win(sub_board)
        else:
            sub_board.mark(row, col, board.current_move)
        board.next_move()
    view = TextView(board)
    view.draw(list(moves[-1][2:]))
    assert capsys.readouterr().out.strip() == board_repr
    