"""
File that genrates and maintaines a board game using pygame.
"""

import pygame
from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard
from ultimate_tic_tac_toe_controller import GraphicalController,\
    TextComputerController

board = UltimateTicTacToeBoard()
player = GraphicalController(board)
AI = TextComputerController(board)

background_colour = (255, 255, 255)

screen = pygame.display.set_mode((520, 600))

# Fill the background colour to the screen
screen.fill(background_colour)

pygame.display.flip()

RUNNING = True

FIRST_BOARD_CHOSEN = False

BOARD_CHOSEN = False

START = False

IS_AI = False

IS_WON = False

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


def draw_subboard(starting_x, starting_y):
    """
    A function that draws the smaller boards that reside within the ultimate
        board.

    Args:
        starting_x: the x-coordinates where the lines will start.
        starting_y: the y-coordinates where the lines will start.
    """
    line_color = (0, 0, 0)

    line_thickness = 5
    square_thickness = 50
    subboard_thickness = line_thickness * 2 + square_thickness * 3
    for line_count in range(2):
        # Draw Vertical Lines for Subboard
        pygame.draw.rect(screen, line_color, pygame.Rect(
            starting_x + square_thickness + line_count * (
                line_thickness +
                square_thickness),
            starting_y, line_thickness,
            subboard_thickness))
        # Draw Horizontal Lines for Subboard
        pygame.draw.rect(screen, line_color, pygame.Rect(
            starting_x, starting_y + square_thickness + line_count *
            (line_thickness + square_thickness), subboard_thickness,
            line_thickness))


def draw_ultimateboard():
    """
    A function that draws the Ultimate Tic Tac Toe Board.
    """
    line_color = (0, 0, 0)

    line_thickness = 8
    square_thickness = 168
    subboard_thickness = line_thickness * 2 + square_thickness * 3
    for line_count in range(2):
        # Draw Vertical Lines for Subboard
        pygame.draw.rect(screen, line_color, pygame.Rect(
            square_thickness + line_count * (
                line_thickness + square_thickness
                + 4), 0, line_thickness - 3, subboard_thickness))
        # Draw Horizontal Lines for Subboard
        pygame.draw.rect(screen, line_color, pygame.Rect(
            0, square_thickness + line_count * (
                line_thickness +
                square_thickness + 4),
            subboard_thickness, line_thickness - 3))


def draw_x(starting_x, starting_y):
    """
    Generates an x using pygame.

    Args:
        starting_x: the x-coordinates where the lines will start.
        starting_y: the y-coordinates where the lines will start.
    """
    line_color = (0, 0, 0)
    line_thickness = 5
    pygame.draw.line(screen, line_color, (starting_x + 5, starting_y + 5),
                     (starting_x + 45, starting_y + 45), width=line_thickness)
    pygame.draw.line(screen, line_color, (starting_x + 45,
                     starting_y + 5), (starting_x + 5, starting_y + 45),
                     width=line_thickness)


def draw_o(starting_x, starting_y):
    """
    Generates an o using pygame.

    Args:
        starting_x: the x-coordinates where the shape will start.
        starting_y: the y-coordinates where the shape will start.
    """
    starting_x += 25
    starting_y += 25
    line_color = (0, 0, 0)
    pygame.draw.circle(screen, line_color,
                       (starting_x, starting_y), 20, width=3)


def mark_square(subboard_coordinates, player):  # pylint: disable=redefined-outer-name
    """
    Marks the square that a player has tapped on.

    Args:
        subboard_coordinates: the coordinates of the section within the small
            game that the player has tapped on.
        player: the mark of the current player that made the current move.
    """
    sub_row, sub_col = subboard_coordinates
    row = sub_row // 3
    col = sub_col // 3

    sub_row = sub_row - row * 3
    sub_col = sub_col - col * 3

    starting_x = sub_col * 55 + col * 180
    starting_y = sub_row * 55 + row * 180
    if player == "X":
        draw_x(starting_x, starting_y)
    else:
        draw_o(starting_x, starting_y)


def ai_move(current_board_position):  # pylint: disable=redefined-outer-name
    """
    Marks the section on the board selected by the AI.

    Args:
        current_board_postition: TO DO
    """
    current_board_square_position, current_board_position = AI.move(
        current_board_position)
    ultimate_row = current_board_position[0] * \
        3 + \
        current_board_square_position[0]   # pylint: disable=redefined-outer-name
    ultimate_col = current_board_position[1] * \
        3 + \
        current_board_square_position[1]  # pylint: disable=redefined-outer-name

    mark_square((ultimate_row, ultimate_col), "O")

    board.next_move()

    if board.check_win():
        win_text(board.current_move)

    if board.check_tie():
        tie_text()

    current_board_position = tuple(current_board_square_position)
    sub_board = board.boards[current_board_position[0]
                             ][current_board_position[1]]  # pylint: disable=redefined-outer-name

    if not board.check_board_availability(sub_board):
        BOARD_CHOSEN = False  # pylint: disable=redefined-outer-name
        return current_board_position, BOARD_CHOSEN
    BOARD_CHOSEN = True
    current_board_text(current_board_position)
    return current_board_position, BOARD_CHOSEN


def current_board_text(current_board_position):  # pylint: disable=redefined-outer-name
    """
    Hi
    """
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = my_font.render(  # pylint: disable=redefined-outer-name
        f'Current board: {current_board_position}', False, (0, 0, 0))
    screen.blit(text_surface, (WIDTH/2 - 90, 555))


def pick_a_board_text():
    """
    Hi
    """
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = my_font.render(  # pylint: disable=redefined-outer-name
        'Choose a valid board!', False, (255, 0, 0))
    screen.blit(text_surface, (WIDTH/2 - 100, 525))


def win_text(winner):
    """
    Hi
    """
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = my_font.render(  # pylint: disable=redefined-outer-name
        f'{winner} Won!', False, (0, 0, 255))
    screen.blit(text_surface, (WIDTH/2 - 50, 555))


def tie_text():
    """
    Hi
    """
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = my_font.render(
        'It\'s a Tie!', False, (0, 0, 255))
    screen.blit(text_surface, (WIDTH/2 - 100, 555))


while RUNNING:

    if board.current_move == "O" and IS_AI:
        current_board_position, BOARD_CHOSEN = ai_move(current_board_position)

    WIDTH = 520
    HEIGHT = 520

    x, y = pygame.mouse.get_pos()

    ultimate_col = int  # pylint: disable=redefined-outer-name
    ultimate_row = int  # pylint: disable=redefined-outer-name

    for i in range(1, 10):
        if x < WIDTH / 9 * i:
            ultimate_col = i - 1
            break
        ultimate_col = None

    for i in range(1, 10):
        if y < HEIGHT / 9 * i:
            ultimate_row = i - 1
            break
        ultimate_row = None

    mouse = pygame.mouse.get_pos()

    if not START:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
            WIDTH/2 - 250, 540, 100, 50))
        text_surface = my_font.render(
            '1 Player', False, (0, 0, 0))
        screen.blit(text_surface, (WIDTH/2 - 240, 555))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
            WIDTH/2 + 150, 540, 100, 50))
        text_surface = my_font.render(
            '2 Player', False, (0, 0, 0))
        screen.blit(text_surface, (WIDTH/2 + 160, 555))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not START:  # pylint: disable=no-member

            if WIDTH/2 - 250 <= mouse[0] <= WIDTH/2 - 150 and 540 <= mouse[1]\
                    <= 590:
                START = True
                IS_AI = True

            if WIDTH/2 + 150 <= mouse[0] <= WIDTH/2 + 250 and 540 <= mouse[1]\
                    <= 590:
                START = True
                IS_AI = False

            pygame.draw.rect(screen, (255, 255, 255),
                             pygame.Rect(0, 520, 520, 80))

        if event.type == pygame.MOUSEBUTTONUP and START and not IS_WON:  # pylint: disable=no-member
            if y > 519:
                break
            if not FIRST_BOARD_CHOSEN:
                sub_board_position = (ultimate_row // 3, ultimate_col // 3)
                player.choose_board(sub_board_position)
                current_board_position = sub_board_position
                FIRST_BOARD_CHOSEN = True
                BOARD_CHOSEN = True
                current_board_text(current_board_position)

            elif not BOARD_CHOSEN:
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
                BOARD_CHOSEN = True
                current_board_text(current_board_position)

            else:
                sub_board_position = (ultimate_row // 3, ultimate_col // 3)
                if sub_board_position != current_board_position:
                    break
                sub_board_square_row = ultimate_row - (ultimate_row // 3) * 3
                sub_board_square_col = ultimate_col - (ultimate_col // 3) * 3

                sub_board_square_position = (
                    sub_board_square_row, sub_board_square_col)

                try:
                    mark_position = player.move(
                        sub_board_position, sub_board_square_position)
                except ValueError:
                    break

                if board.current_move == "X":
                    mark_square((ultimate_row, ultimate_col), "X")
                else:
                    mark_square((ultimate_row, ultimate_col), "O")
                if board.check_win():
                    win_text(board.current_move)
                    IS_WON = True
                    continue
                if board.check_tie():
                    tie_text()
                    IS_WON = True
                    continue
                board.next_move()
                current_board_position = sub_board_square_position
                current_board_text(current_board_position)
                sub_board = board.boards[current_board_position[0]
                                         ][current_board_position[1]]
                if not board.check_board_availability(sub_board):
                    BOARD_CHOSEN = False
                    break

        if event.type == pygame.quit:  # pylint: disable=no-member
            RUNNING = False

    draw_ultimateboard()
    for i in range(3):
        for j in range(3):
            draw_subboard(i * 180, j * 180)

    if not BOARD_CHOSEN and board.current_move == "X" and START:
        pick_a_board_text()
    else:
        text_surface = my_font.render(
            "Choose a valid board!", False, (255, 255, 255))
        screen.blit(text_surface, (WIDTH/2 - 100, 525))
    pygame.display.flip()
