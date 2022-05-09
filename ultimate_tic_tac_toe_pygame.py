"""
File that genrates and maintaines a board game using pygame.
"""

import pygame
from pygame_functions import draw_subboard, draw_ultimateboard, \
    mark_square, ai_move, current_board_text, pick_a_board_text, \
    draw_menu, win_text, tie_text
from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard
from ultimate_tic_tac_toe_controller import GraphicalController,\
    TextComputerController


def main():
    """
    Main pygame loop.
    """
    board = UltimateTicTacToeBoard()
    player = GraphicalController(board)
    ai_player = TextComputerController(board)

    background_colour = (255, 255, 255)

    screen = pygame.display.set_mode((520, 600))

    # Fill the background colour to the screen
    screen.fill(background_colour)

    pygame.display.flip()

    running = True

    first_board_chosen = False

    board_chosen = False

    start = False

    is_ai = False

    is_won = False

    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    while running:

        if board.current_move == "O" and is_ai:
            current_board_position, board_chosen = ai_move(
                current_board_position, board, ai_player)

        width = 520
        height = 520

        x_pos, y_pos = pygame.mouse.get_pos()

        ultimate_col = int  # pylint: disable=redefined-outer-name
        ultimate_row = int  # pylint: disable=redefined-outer-name

        for i in range(1, 10):
            if x_pos < width / 9 * i:
                ultimate_col = i - 1
                break
            ultimate_col = None

        for i in range(1, 10):
            if y_pos < height / 9 * i:
                ultimate_row = i - 1
                break
            ultimate_row = None

        mouse = pygame.mouse.get_pos()

        if not start:
            draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable=no-member
                running = False
                continue

            if event.type == pygame.MOUSEBUTTONDOWN and not start:  # pylint: disable=no-member

                if width/2 - 250 <= mouse[0] <= width/2 - 150 and \
                        540 <= mouse[1] <= 590:
                    start = True
                    is_ai = True

                if width/2 + 150 <= mouse[0] <= width/2 + 250 and \
                        540 <= mouse[1] <= 590:
                    start = True
                    is_ai = False

                pygame.draw.rect(screen, (255, 255, 255),
                                 pygame.Rect(0, 520, 520, 80))

            if event.type == pygame.MOUSEBUTTONUP and start and not is_won:  # pylint: disable=no-member
                if y_pos > 519:
                    break
                if not first_board_chosen:
                    sub_board_position = (ultimate_row // 3, ultimate_col // 3)
                    player.choose_board(sub_board_position)
                    current_board_position = sub_board_position
                    first_board_chosen = True
                    board_chosen = True
                    current_board_text(current_board_position)

                elif not board_chosen:
                    sub_board_position = (ultimate_row // 3, ultimate_col // 3)
                    sub_board = board.boards[sub_board_position[0]
                                             ][sub_board_position[1]]
                    if not board.check_board_availability(sub_board):
                        try:
                            sub_board_position = player.choose_board(
                                sub_board_position)
                        except ValueError:
                            break
                    current_board_position = sub_board_position
                    board_chosen = True
                    current_board_text(current_board_position)

                else:
                    sub_board_position = (ultimate_row // 3, ultimate_col // 3)
                    if sub_board_position != current_board_position:
                        break
                    sub_board_square_row = ultimate_row - \
                        (ultimate_row // 3) * 3
                    sub_board_square_col = ultimate_col - \
                        (ultimate_col // 3) * 3

                    sub_board_square_position = (
                        sub_board_square_row, sub_board_square_col)

                    try:
                        _ = player.move(
                            sub_board_position, sub_board_square_position)
                    except ValueError:
                        break

                    if board.current_move == "X":
                        mark_square((ultimate_row, ultimate_col), "X")
                    else:
                        mark_square((ultimate_row, ultimate_col), "O")
                    if board.check_win():
                        win_text(board.current_move)
                        is_won = True
                        continue
                    if board.check_tie():
                        tie_text()
                        is_won = True
                        continue
                    board.next_move()
                    current_board_position = sub_board_square_position
                    current_board_text(current_board_position)
                    sub_board = board.boards[current_board_position[0]
                                             ][current_board_position[1]]
                    if not board.check_board_availability(sub_board):
                        board_chosen = False
                        break

        draw_ultimateboard()
        for i in range(3):
            for j in range(3):
                draw_subboard(i * 180, j * 180)

        if not board_chosen and board.current_move == "X" and start:
            pick_a_board_text()
        else:
            text_surface = my_font.render(
                "Choose a valid board!", False, (255, 255, 255))
            screen.blit(text_surface, (width/2 - 100, 525))
        pygame.display.flip()

    pygame.quit()  # pylint: disable=no-member


# call the main function
if __name__ == "__main__":
    main()
