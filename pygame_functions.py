"""
Functions that handle pygame related tasks and AI player input.
"""
import pygame

SCREEN = pygame.display.set_mode((520, 600))
WIDTH = 520
pygame.font.init()
MY_FONT = pygame.font.SysFont('Comic Sans MS', 30)


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
        pygame.draw.rect(SCREEN, line_color, pygame.Rect(
            starting_x + square_thickness + line_count * (
                line_thickness +
                square_thickness),
            starting_y, line_thickness,
            subboard_thickness))
        # Draw Horizontal Lines for Subboard
        pygame.draw.rect(SCREEN, line_color, pygame.Rect(
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
        pygame.draw.rect(SCREEN, line_color, pygame.Rect(
            square_thickness + line_count * (
                line_thickness + square_thickness
                + 4), 0, line_thickness - 3, subboard_thickness))
        # Draw Horizontal Lines for Subboard
        pygame.draw.rect(SCREEN, line_color, pygame.Rect(
            0, square_thickness + line_count * (
                line_thickness +
                square_thickness + 4),
            subboard_thickness, line_thickness - 3))


def draw_x(starting_x, starting_y):
    """
    Generates an X using pygame.

    Args:
        starting_x: the x-coordinates where the lines will start.
        starting_y: the y-coordinates where the lines will start.
    """
    line_color = (0, 0, 0)
    line_thickness = 5
    pygame.draw.line(SCREEN, line_color, (starting_x + 5, starting_y + 5),
                     (starting_x + 45, starting_y + 45), width=line_thickness)
    pygame.draw.line(SCREEN, line_color, (
        starting_x + 45,
        starting_y + 5), (starting_x + 5, starting_y + 45),
        width=line_thickness)


def draw_o(starting_x, starting_y):
    """
    Generates an O using pygame.

    Args:
        starting_x: the x-coordinates where the shape will start.
        starting_y: the y-coordinates where the shape will start.
    """
    starting_x += 25
    starting_y += 25
    line_color = (0, 0, 0)
    pygame.draw.circle(SCREEN, line_color,
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


def ai_move(current_board_position, board, ai_player):  # pylint: disable=redefined-outer-name
    """
    Marks the section on the board selected by the AI. Also checks
    for win conditions, tie conditions, and if the player needs
    to select a new board after the AI plays.

    Args:
        current_board_postition: A tuple that contains two integers representing
            the indicies where the sub board is located within the
            ultimate tic-tac-toe-board.
            board: An UltimateTicTacToeBoard instance.
            ai_player: A TextComputerController instance.

    Returns:
        A tuple containing:
            A tuple that contains two integers representing
            the indicies where the sub board is located within the
            ultimate tic-tac-toe-board.
            A boolean representing if a board needs to be chosen.
    """
    current_board_square_position, current_board_position = ai_player.move(
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
        board_chosen = False  # pylint: disable=redefined-outer-name
        return current_board_position, board_chosen
    board_chosen = True
    current_board_text(current_board_position)
    return current_board_position, board_chosen


def current_board_text(current_board_position):  # pylint: disable=redefined-outer-name
    """
    Draws text indicating the current sub boad in play.

    Args:
        current_board_postition: A tuple that contains two integers
            representing the indicies where the sub board is located
            within the ultimate tic-tac-toe-board.
    """
    pygame.draw.rect(SCREEN, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = MY_FONT.render(  # pylint: disable=redefined-outer-name
        f'Current board: {current_board_position}', False, (0, 0, 0))
    SCREEN.blit(text_surface, (WIDTH/2 - 90, 555))


def pick_a_board_text():
    """
    Draws text to indicate that a player needs to chose a new sub board.
    """
    pygame.draw.rect(SCREEN, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = MY_FONT.render(  # pylint: disable=redefined-outer-name
        'Choose a valid board!', False, (255, 0, 0))
    SCREEN.blit(text_surface, (WIDTH/2 - 100, 525))


def draw_menu():
    """
    Draws the two buttons at the start which allow for singleplayer against
    an AI or two player.
    """
    pygame.draw.rect(SCREEN, (255, 0, 0), pygame.Rect(
        WIDTH/2 - 250, 540, 100, 50))
    text_surface = MY_FONT.render(
        '1 Player', False, (0, 0, 0))
    SCREEN.blit(text_surface, (WIDTH/2 - 240, 555))

    pygame.draw.rect(SCREEN, (255, 0, 0), pygame.Rect(
        WIDTH/2 + 150, 540, 100, 50))
    text_surface = MY_FONT.render(
        '2 Player', False, (0, 0, 0))
    SCREEN.blit(text_surface, (WIDTH/2 + 160, 555))


def win_text(winner):
    """
    Draws text when a player wins indicating a win.
    """
    pygame.draw.rect(SCREEN, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = MY_FONT.render(  # pylint: disable=redefined-outer-name
        f'{winner} Won!', False, (0, 0, 255))
    SCREEN.blit(text_surface, (WIDTH/2 - 50, 555))


def tie_text():
    """
    Draws text when both players tie indicating a tie.
    """
    pygame.draw.rect(SCREEN, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = MY_FONT.render(
        'It\'s a Tie!', False, (0, 0, 255))
    SCREEN.blit(text_surface, (WIDTH/2 - 100, 555))
