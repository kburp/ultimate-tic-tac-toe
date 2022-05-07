"""
Unit tests for ultimate tic tac toe controller.
"""

import io
import pytest
from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard
from ultimate_tic_tac_toe_controller import TextController


@pytest.fixture()
def board():
    """
    Create an ultimate tic tac toe board for use in testing.
    """
    return UltimateTicTacToeBoard()


def test_one_move(board, monkeypatch):
    """
    Test that selecting a subboard and a square in that board marks the
    appropriate square.

    Args:
        board: The UltimateTicTacToeBoard instance used.
        monkeypatch: An object that helps to simulate user input.
    """
    input = ("1 1", "1 1")
    move = ((1, 1, 1, 1), "X")

    controller = TextController(board)

    monkeypatch.setattr("sys.stdin", io.StringIO(input[0]))
    sub_board_position = controller.choose_board()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[1]))
    controller.move(sub_board_position)

    assert board.boards[move[0][0]][move[0][1]
                                    ]._board_state[move[0][2]][move[0][3]] == move[1]


def test_two_moves(board, monkeypatch):
    """
    Test that selecting a subboard and selecting a square from two player
    marks the appropriate squares.

    Args:
        board: The UltimateTicTacToeBoard instance used.
        monkeypatch: An object that helps to simulate user input.
    """
    input = ("1 1", "1 1", "2 2")
    move = ((1, 1, 1, 1), "X", (1, 1, 2, 2), "O")

    controller = TextController(board)

    monkeypatch.setattr("sys.stdin", io.StringIO(input[0]))
    sub_board_position = controller.choose_board()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[1]))
    controller.move(sub_board_position)
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[2]))
    controller.move(sub_board_position)
    assert board.boards[move[0][0]][move[0][1]]._board_state[move[0][2]][move[0][3]] == move[1] and board.boards[move[2][0]][move[2][1]
                                                                                                                             ]._board_state[move[2][2]][move[2][3]] == move[3]


def test_invalid_char_input(board, monkeypatch):
    """
    Test that an invalid input containing non-numeric characters
    is gracefully handled without uncaught exceptions.

    Args:
        board: The UltimateTicTacToeBoard instance used.
        monkeypatch: An object that helps to simulate user input.
    """
    input = ("hello world", "1 1", "1 1", "2 2")
    move = ((1, 1, 1, 1), "X", (1, 1, 2, 2), "O")

    controller = TextController(board)

    monkeypatch.setattr("sys.stdin", io.StringIO(input[0]))
    monkeypatch.setattr("sys.stdin", io.StringIO(input[1]))
    sub_board_position = controller.choose_board()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[2]))
    controller.move(sub_board_position)
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[3]))
    controller.move(sub_board_position)
    assert board.boards[move[0][0]][move[0][1]]._board_state[move[0][2]][move[0][3]] == move[1] and board.boards[move[2][0]][move[2][1]
                                                                                                                             ]._board_state[move[2][2]][move[2][3]] == move[3]


def test_invalid_num_input(board, monkeypatch):
    """
    Test that an invalid input containing numeric characters out of the
    row and column index are gracefully handled without uncaught exceptions.

    Args:
        board: The UltimateTicTacToeBoard instance used.
        monkeypatch: An object that helps to simulate user input.
    """
    input = ("3948 -3944", "1 1", "1 1", "2 2")
    move = ((1, 1, 1, 1), "X", (1, 1, 2, 2), "O")

    controller = TextController(board)

    monkeypatch.setattr("sys.stdin", io.StringIO(input[0]))
    monkeypatch.setattr("sys.stdin", io.StringIO(input[1]))
    sub_board_position = controller.choose_board()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[2]))
    controller.move(sub_board_position)
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[3]))
    controller.move(sub_board_position)
    assert board.boards[move[0][0]][move[0][1]]._board_state[move[0][2]][move[0][3]] == move[1] and board.boards[move[2][0]][move[2][1]

                                                                                                                             ]._board_state[move[2][2]][move[2][3]] == move[3]


def test_invalid_square_input(board, monkeypatch):
    """
    Test that a square that has already been marked cannot be marked again.

    Args:
        board: The UltimateTicTacToeBoard instance used.
        monkeypatch: An object that helps to simulate user input.
    """
    input = ("1 1", "1 1", "1 1", "1 1")
    move = ((1, 1, 1, 1), "X")

    controller = TextController(board)

    monkeypatch.setattr("sys.stdin", io.StringIO(input[0]))
    sub_board_position = controller.choose_board()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[1]))
    controller.move(sub_board_position)
    monkeypatch.setattr("sys.stdin", io.StringIO(input[2]))
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[3]))
    assert board.boards[move[0][0]][move[0][1]
                                    ]._board_state[move[0][2]][move[0][3]] == move[1]


def test_invalid_mark_on_won_subboard(board, monkeypatch):
    """
    Test that a square that has already been marked cannot be marked again.

    Args:
        board: The UltimateTicTacToeBoard instance used.
        monkeypatch: An object that helps to simulate user input.
    """
    input = ("1 1", "1 1", "2 2", "1 1", "2 1",
             "1 1", "2 0", "1 1", "1 1", "0 0", "0 0")
    move = ((0, 0, 0, 0), "O")

    controller = TextController(board)

    monkeypatch.setattr("sys.stdin", io.StringIO(input[0]))
    sub_board_position = controller.choose_board()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[1]))
    controller.move(sub_board_position)
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[2]))
    controller.move((1, 1))
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[3]))
    controller.move((2, 2))
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[4]))
    controller.move((1, 1))
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[5]))
    controller.move((2, 1))
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[6]))
    controller.move((1, 1))
    board.next_move()
    monkeypatch.setattr("sys.stdin", io.StringIO(input[7]))
    controller.move((2, 0))
    monkeypatch.setattr("sys.stdin", io.StringIO(input[8]))
    monkeypatch.setattr("sys.stdin", io.StringIO(input[9]))
    controller.choose_board()
    board.next_move()

    assert board.boards[move[0][0]][move[0][1]
                                    ]._board_state[move[0][2]][move[0][3]] == ' '
