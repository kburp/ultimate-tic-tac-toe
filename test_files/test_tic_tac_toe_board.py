"""
Unit tests for tic tac toe board.
"""

import pytest
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


# Test various reprs
# Test check win for various board states
# Test check tie for various board states
# Test marking on an empty board
# Test marking twice in the same spot
# Test marking on a square that is already taken
# Check board state at the beginning of the game