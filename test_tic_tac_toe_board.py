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


board_states = [
    # Horizontal win
    ([(0, 1, "X"), (2, 1, "O"), (0, 0, "X"), (0, 2, "X")], "X"),
    ([(0, 0, "O"), (0, 1, "O"), (0, 2, "O")], "O"),
    ([(1, 1, "O"), (2, 2, "O"), (2, 1, "O"), (1, 0, "X"), (2, 0, "O")], "O"),
    ([(0, 2, "O"), (1, 2, "X"), (2, 2, "O"), (1, 1, "X"), (0, 0, "O"), \
        (1, 0, "X")], "X"),
    # Vertical win
    ([(2, 2, "X"), (0, 2, "X"), (1, 2, "X")], "X"),
    ([(2, 2, "X"), (1, 2, "O"), (2, 0, "X"), (0, 1, "O"), (1, 1, "O"), \
        (2, 1, "O")], "O"),
    ([(0, 0, "O"), (0, 1, "X"), (2, 0, "O"), (1, 0, "O")], "O"),
    # Diagonal win
    ([(1, 1, "O"), (1, 0, "X"), (2, 0, "X"), (0, 0, "O"), (2, 2, "O")], "O"),
    ([(0, 2, "X"), (1, 1, "X"), (2, 0, "X")], "X"),
    #Tie
    ([(0, 0, "X"), (1, 1, "O"), (1, 0, "X"), (2, 0, "O"), (0, 2, "X"), \
        (0, 1, "O"), (2, 1, "X"), (1, 2, "O"), (2, 2, "X")], "Tie"),
    ([(0, 0, "O"), (1, 0, "O"), (2, 0, "X"), (0, 1, "X"), (1, 1, "O"), \
        (2, 1, "O"), (0, 2, "O"), (1, 2, "X"), (2, 2, "X")], "Tie"),
    # No winner (board not full yet)
    ([], None),
    ([(1, 1, "X")], None),
    ([(0, 0, "O"), (0, 1, "O"), (0, 2, "X")], None),
    ([(0, 0, "X"), (0, 1, "X"), (1, 0, "X"), (2, 2, "X"), (2, 1, "X")], None),
    ([(0, 0, "O"), (1, 1, "X"), (2, 2, "O"), (0, 2, "O"), (2, 0, "O")], None)
]

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


def test_mark_empty(board, row, col, player): # pylint: disable=redefined-outer-name
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


def test_mark_taken(board, row, col, player): # pylint: disable=redefined-outer-name
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


def test_start_with_empty_board(board, row, col): # pylint: disable=redefined-outer-name
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


def test_check_win(board, game): # pylint: disable=redefined-outer-name
    """
    Test that the board correctly detects wins in various conditions.

    Args:
        board: The TicTacToeBoard instance to use.
        game: A tuple where the first element is a list of moves to be made in
            the game, and the second element is a string representing the
            winner of the game after those moves (or None if the game ends with
            no winner, or "Tie" if the game is a tie).
    """
    moves, expected_winner = game
    for row, col, player in moves:  # pylint: disable=redefined-outer-name
        assert not board.check_win("X")
        assert not board.check_win("O")
        board.mark(row, col, player)
    if expected_winner is None or expected_winner == "Tie":
        assert not board.check_win("X")
        assert not board.check_win("O")
    else:
        assert board.check_win(expected_winner)


def test_check_tie(board, game): # pylint: disable=redefined-outer-name
    """
    Test that the board correctly detects ties.

    Args:
        board: The TicTacToeBoard instance to use.
        game: A tuple where the first element is a list of moves to be made in
            the game, and the second element is a string representing the
            winner of the game after those moves (or None if the game ends with
            no winner, or "Tie" if the game is a tie).
    """
    moves, expected_winner = game
    for row, col, player in moves: # pylint: disable=redefined-outer-name
        assert not board.check_tie()
        board.mark(row, col, player)
    if expected_winner == "Tie":
        assert board.check_tie()
    else:
        assert not board.check_tie()
