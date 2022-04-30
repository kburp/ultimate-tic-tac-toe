"""
Main program to set up and run an ultimate tic-tac-toe game.
"""
from operator import sub
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

    while True:
        try:
            sub_board_position = input(
                "Choose the row and column of the starting board (0 - 2): ")
            sub_board_position = [int(x) for x in sub_board_position.split()]
            if (0 <= sub_board_position[0] <= 2) and (0 <= sub_board_position[1] <= 2):
                break
        except:
            print(f"{sub_board_position} was not a valid move.")

    while True:
        sub_board = board.boards[sub_board_position[0]][sub_board_position[1]]
        if sub_board.won == True:
            sub_board_position = textController.choose_board()
        sub_board_position = textController.move(sub_board_position)
        if board.check_win():
            print(f"{board.current_move} won!")
            break
        board.next_move()
        textView.draw()


if __name__ == "__main__":
    main()
