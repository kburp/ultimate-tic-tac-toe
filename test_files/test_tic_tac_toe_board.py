"""
Unit tests for tic tac toe board.
"""

import pytest
import sys

from regex import D
sys.path.append("../ultimate-tic-tac-toe")
from tic_tac_toe_board import TicTacToeBoard

@pytest.fixture
def board():
    """
    Create a tic tac toe board for use in testing.
    """
    return TicTacToeBoard()


@pytest.fixture(params=["X", "O"])
def player(request):
    """
    Create a player for use in testing.
    """
    return request.param


@pytest.fixture(params=range(3))
def row(request):
    """
    Create a row index for use in testing.
    """
    return request.param


@pytest.fixture(params=range(3))
def col(request):
    """
    Create a column index for use in testing.
    """
    return request.param

# add cases to this list
board_states = []

@pytest.fixture(params=board_states)
def game(request):
    """
    Create a sequence of moves representing a game for use in testing.
    """
    return request.param

# add cases to this list
board_reprs = []

@pytest.fixture(params=board_reprs)
def game_repr(request):
    """
    Create a representation of a sequence of moves for use in testing.
    """
    return request.param


def test_mark_empty(board, row, col, player):
    """
    Test that marking an empty square places does not return an error.

    Args:
        board: The TicTacToeBoard instance to use.
        row: An integer representing the row index.
        col: An integer representing the column index.
        player: A string representing the marking symbol of the current player.
    """
    board.mark(row, col, player)
    assert True


def test_mark_taken(board, row, col, player):
    """
    Test that marking a taken space causes an error.

    Args:
        board: The TicTacToeBoard instance to use.
        row: An integer representing the row index.
        col: An integer representing the column index.
        player: A string representing the marking symbol of the current player.
    """
    board.mark(row, col, player)
    with pytest.raises(ValueError):
        board.mark(row, col, player)


def test_start_with_empty_board(board, row, col):
    """
    Test that at the start of the game, all squares are blank.

    Args:
        board: The TicTacToeBoard instance to use.
        row: An integer representing the row index.
        col: An integer representing the column index.
    """
    assert board.get_square(row, col) == " "


def test_mark_result(board, row, col, player):  # pylint: disable=redefined-outer-name
    """
    Test that after marking an available square, the player's mark used is
    returned by get_square.

    Args:
        board: The TicTacToeBoard instance to use.
        row: An integer representing the row index.
        col: An integer representing the column index.
        player: A string representing the marking symbol of the current player.
    """
    board.mark(row, col, player)
    assert board.get_square(row, col) == player

# Test various reprs
# Test check win for various board states
# Test check tie for various board states