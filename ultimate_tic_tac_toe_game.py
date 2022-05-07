"""
Main program to set up and run an ultimate tic-tac-toe game.
"""

from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard
from ultimate_tic_tac_toe_view import TextView
from ultimate_tic_tac_toe_controller import TextComputerController, TextController


def main():
    """
    Your docstring goes here.
    """
    print("\nWelcome to ultimate tic tac toe!")
    print("Enter \'1\' to play against the computer.")
    print("Enter \'2\' to play a two player game.")

    while True:
        how_many_players = input("Number of players: ")
        if how_many_players in ("1", "2"):
            break

    board = UltimateTicTacToeBoard()
    textView = TextView(board)
    player_one = TextController(board)

    if how_many_players == "1":
        player_two = TextComputerController(board)
    else:
        player_two = TextController(board)

    sub_board_position = None
    while sub_board_position == None:
        try:
            sub_board_position = player_two.choose_board()
        except ValueError:
            pass

    while True:
        sub_board = board.boards[sub_board_position[0]][sub_board_position[1]]
        if not board.check_board_availability(sub_board):
            sub_board_position = None
            while sub_board_position == None:
                try:
                    sub_board_position = player_one.choose_board()
                except ValueError:
                    pass
            continue

        mark_position = None
        while mark_position == None:
            try:
                mark_position = player_one.move(sub_board_position)
            except ValueError:
                pass

        if board.check_win():
            print(f"{board.current_move} won!")
            break
        if board.check_tie():
            print("It's a tie!")
            break

        board.next_move()

        textView.draw(sub_board_position)

        sub_board = board.boards[sub_board_position[0]][sub_board_position[1]]
        while (not board.check_board_availability(sub_board)) and \
                isinstance(player_two, TextController):

            sub_board_position = None
            while sub_board_position == None:
                try:
                    sub_board_position = player_two.choose_board()
                except ValueError:
                    pass
            sub_board = board.boards[sub_board_position[0]][
                sub_board_position[1]]

        mark_position = None
        while mark_position == None:
            try:
                mark_position = player_two.move(sub_board_position)
            except ValueError:
                pass

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
