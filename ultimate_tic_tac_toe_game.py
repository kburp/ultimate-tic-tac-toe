"""
Main program to set up and run an ultimate tic-tac-toe game.
"""

from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard
from ultimate_tic_tac_toe_view import TextView
from ultimate_tic_tac_toe_controller import TextComputerController, \
    TextController


def main(): # pylint: disable=too-many-branches, disable=too-many-statements
    """
    Main function to run the game.
    """
    # print introduction message
    print("\nWelcome to ultimate tic tac toe!")
    print("Enter \'1\' to play against the computer.")
    print("Enter \'2\' to play a two player game.")

    #set number of players
    while True:
        how_many_players = input("Number of players: ")
        if how_many_players in ("1", "2"):
            break

    # create model, view, and controller for the game
    board = UltimateTicTacToeBoard()
    text_view = TextView(board)
    player_one = TextController(board)

    # create a second controller that is either human or computer.
    if how_many_players == "1":
        player_two = TextComputerController(board)
    else:
        player_two = TextController(board)

    sub_board_position = None
    # choose an initial sub_board
    while sub_board_position is None:
        try:
            sub_board_position = player_one.choose_board()
        except ValueError:
            pass

    # main game loop
    while True:
        # set sub_board
        sub_board = board.boards[sub_board_position[0]][sub_board_position[1]]
        # check availability of selected sub board
        if not board.check_board_availability(sub_board):
            sub_board_position = None
            while sub_board_position is None:
                try:
                    sub_board_position = player_one.choose_board()
                except ValueError:
                    pass
            continue

        mark_position = None
        # try marking a position
        while mark_position is None:
            try:
                mark_position, _ = player_one.move(sub_board_position)
            except ValueError:
                pass

        # set the next sub_board position to the position on the sub_board
        # that was just marked
        sub_board_position = mark_position

        # end the game if there is a win or tie
        if board.check_win():
            print(f"{board.current_move} won!")
            break
        if board.check_tie():
            print("It's a tie!")
            break

        # update whose turn it is
        board.next_move()

        # call the view class
        text_view.draw(sub_board_position)

        # select the next sub_board to play on
        sub_board = board.boards[sub_board_position[0]][sub_board_position[1]]
        while (not board.check_board_availability(sub_board)) and \
                isinstance(player_two, TextController):

            sub_board_position = None
            while sub_board_position is None:
                try:
                    sub_board_position = player_two.choose_board()
                except ValueError:
                    pass
            sub_board = board.boards[sub_board_position[0]][
                sub_board_position[1]]

        mark_position = None
        # mark a position on the board
        while mark_position is None:
            try:
                print(sub_board_position)
                mark_position, _ = player_two.move(sub_board_position)
            except ValueError:
                pass

        # set the next sub_board position to the position on the sub_board
        # that was just marked
        sub_board_position = mark_position

        # end the game if there is a win or tie
        if board.check_win():
            print(f"{board.current_move} won!")
            break
        if board.check_tie():
            print("It's a tie!")
            break

        # update whose turn it is
        board.next_move()

        # display the current state of the board
        text_view.draw(sub_board_position)


# call the main function
if __name__ == "__main__":
    main()
