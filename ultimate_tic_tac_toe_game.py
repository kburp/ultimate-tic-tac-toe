"""
Main program to set up and run an ultimate tic-tac-toe game.
"""
from operator import sub

from numpy import choose
from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard
from ultimate_tic_tac_toe_view import TextView
from ultimate_tic_tac_toe_controller import TextController


def main():
    """
    Your docstring goes here.
    """
    board = UltimateTicTacToeBoard()
    textController = TextController(board)
    textView = TextView(board)

    sub_board_position = textController.choose_board()

    while True:
        sub_board = board.boards[sub_board_position[0]][sub_board_position[1]]
        if board.check_board_availability(sub_board):
            sub_board_position = textController.choose_board()
            continue

        sub_board_position = textController.move(sub_board_position)

        if board.check_win():
            print(f"{board.current_move} won!")
            break
        if board.check_tie():
            print("It's a tie!")
            break

        board.next_move()

        textView.draw(sub_board_position)


if __name__ == "__main__":
    main()
