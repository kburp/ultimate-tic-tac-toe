"""
Unit tests for ultimate tic tac toe board.
"""
import pytest
from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard


@pytest.fixture()
def board():
    """
    Create an ultimate tic tac toe board for use in testing.
    """
    return UltimateTicTacToeBoard()


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


win_states = [
    ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
    (("X", 1, "X"), ("O", "O", 1), ("X", 1, "O")),
    ((0, "O", "X"), (0, 0, 1), ("X", "X", 0))
]


@pytest.fixture(params=win_states)
def board_availability(request):
    """
    Create a set of board availability states for testing.
    """
    return request.param


# add cases to this list
board_states = [
    # Horizontal win
    ([("X", "X", "X"), (0, 1, "O"), ("O", 1, 1)], "X"),
    ([(0, 0, 0), ("O", "O", "O"), (1, 1, 1)], "O"),
    ([(1, 0, "X"), ("X", "O", "O"), ("X", "X", "X")], "X"),
    # Vertical win
    ([("O", "X", 1), ("O", 0, 0), ("O", "X", "X")], "O"),
    ([("O", "X", 1), ("O", "X", 1), (0, "X", 0)], "X"),
    ([(0, 0, "X"), (1, "O", "X"), (1, 0, "X")], "X"),
    # Diagonal win
    ([("O", 1, 0), ("X", "O", "X"), (0, 1, "O")], "O"),
    ([("O", "O", "X"), ("O", "X", 1), ("X", 1, 1)], "X"),
    # Tie
    ([(1, 1, 1), (1, 1, 1), (1, 1, 1)], False),
    ([("X", "O", "X"), ("O", "O", "X"), ("O", "X", "O")], False),
    ([(1, "X", "X"), ("X", "O", 1), (1, "O", "O")], False),
    # No winner (board not full yet)
    ([(0, 0, 0), (0, 0, 0), (0, 0, 0)], False),
    ([(0, "X", 0), (1, 1, "O"), ("O", "O", "X")], False),
    ([("O", 1, "O"), (0, "O", "X"), (0, 0, 0)], False)
]


@pytest.fixture(params=board_states)
def game(request):
    """
    Create another set of board states for testing checking wins.
    """
    return request.param


board_reprs = [
    ([],    "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"
            "| | | || | | || | | |\n"
            "+-+-+-++-+-+-++-+-+-+\n"),
    ([(0, 0, 0, 0), (0, 0, 1, 1), (1, 1, 2, 1)],    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "|X| | || | | || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "| |O| || | | || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "| | | || | | || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "| | | || | | || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "| | | || | | || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "| | | || |X| || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "| | | || | | || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "| | | || | | || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"
                                                    "| | | || | | || | | |\n"
                                                    "+-+-+-++-+-+-++-+-+-+\n"),
    ([(0, 0, 0, 0), (0, 0, 3, 3), (1, 1, 1, 2), (1, 1, 3, 3), (2, 1, 0, 0),
        (2, 2, 3, 3)],
        "+-+-+-++-+-+-++-+-+-+\n"
        "|O|O|O|| | | || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "|O| |O|| | | || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "|O|O|O|| | | || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | ||X| |X|| | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | || |X| || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | ||X| |X|| | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | ||X| | ||O|O|O|\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | || | | ||O| |O|\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | || | | ||O|O|O|\n"
        "+-+-+-++-+-+-++-+-+-+\n"),
    ([(0, 0, 0, 0), (0, 0, 2, 2), (2, 2, 1, 2), (1, 2, 1, 1), (1, 1, 1, 1),
        (1, 1, 0, 0), (0, 0, 1, 0), (1, 0, 2, 2), (2, 2, 0, 2),
        (0, 2, 1, 0)],
        "+-+-+-++-+-+-++-+-+-+\n"
        "|X| | || | | || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "|X| | || | | ||O| | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | |O|| | | || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | ||O| | || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | || |X| || |O| |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | |O|| | | || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | || | | || | |X|\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | || | | || | |X|\n"
        "+-+-+-++-+-+-++-+-+-+\n"
        "| | | || | | || | | |\n"
        "+-+-+-++-+-+-++-+-+-+\n"),
]


@pytest.fixture(params=board_reprs)
def game_repr(request):
    """
    Create a representation of a sequence of moves for use in testing.
    """
    return request.param


def test_next_move(board):  # pylint: disable=redefined-outer-name
    """
    Test that after calling the next_move method, the current player is
    updated.

    Args:
        board: The UltimateTicTacToeBoard instance to use.
    """
    for i in range(0, 81):
        if i % 2 == 0:
            assert board.current_move == "X"
        else:
            assert board.current_move == "O"
        board.next_move()


def test_check_board_availability(board, row, col, board_availability):  # pylint: disable=redefined-outer-name
    """
    Test that UltimateTicTacToeBoard correctly determines whether or not
    a sub-board is available to play on.

    Args:
        board: The UltimateTicTacToeBoard instance to use.
        row: An int representing the row index of a given sub-board.
        col: An int representing the column index of a given sub-board.
        board_availability: A list of tuples containing tuples that represent
        win states for all nine sub-boards in an UltimateTicTacToeBoard.
    """
    sub_board = board.get_board(row, col)
    assert board.check_board_availability(sub_board)
    sub_board.win_state = board_availability[row][col]
    if board_availability[row][col] == 0:
        assert board.check_board_availability(sub_board)
    else:
        assert not board.check_board_availability(sub_board)


def test_check_tie(board, game):  # pylint: disable=redefined-outer-name
    """
    Add docstring.
    """
    pass


def test_check_win(board, game):  # pylint: disable=redefined-outer-name
    """
    Test that UltimateTicTacToeBoard correctly determines a win.

    Args:
        board: The UltimateTicTacToeBoard instance to use.
        game: A tuple where the first element is a list representing the win
            states of each sub-board in the UltimateTicTacToeBoard, and the
            second element is a string or boolean representing the expected
            output of the check_win function for that particular board win
            state configuration.
    """
    assert not board.check_win()
    win_states, expected_output = game  # pylint: disable=redefined-outer-name
    for i, row in enumerate(win_states):  # pylint: disable=redefined-outer-name
        for j, state in enumerate(row):
            sub_board = board.get_board(i, j)
            sub_board.win_state = state
    assert board.check_win() == expected_output


def test_repr(board, game_repr):  # pylint: disable=redefined-outer-name
    """
    Test that the string representation of the board at various stages of the
    game is correct.

    Args:
        board: The UltimateTicTacToeBoard instance to use.
        game_repr: A tuple where the first element is a list of tuples
            containing row and column indices to mark a move, and the second
            element is a string representing the expected output of the repr
            method after those moves are made.
    """
    moves, board_repr = game_repr
    for board_row, board_column, row, col in moves:  # pylint: disable=redefined-outer-name
        sub_board = board.get_board(board_row, board_column)
        if row == col == 3:
            board.mark_win(sub_board)
        else:
            sub_board.mark(row, col, board.current_move)
            board.next_move()
    assert str(board) == board_repr
