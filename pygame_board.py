
# import the pygame module
from sqlalchemy import false
from ultimate_tic_tac_toe_board import UltimateTicTacToeBoard
from ultimate_tic_tac_toe_controller import GraphicalController, TextComputerController
from click import pass_obj
import pygame
import time

board = UltimateTicTacToeBoard()
player = GraphicalController(board)
AI = TextComputerController(board)

background_colour = (255, 255, 255)

screen = pygame.display.set_mode((520, 600))

# Fill the background colour to the screen
screen.fill(background_colour)

pygame.display.flip()

running = True

first_board_chosen = False

board_chosen = False

start = False

is_AI = False

is_won = False

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


def draw_subboard(starting_x, starting_y):
    line_color = (0, 0, 0)

    line_thickness = 5
    square_thickness = 50
    subboard_thickness = line_thickness * 2 + square_thickness * 3
    for line_count in range(2):
        # Draw Vertical Lines for Subboard
        pygame.draw.rect(screen, line_color, pygame.Rect(
            starting_x + square_thickness + line_count * (line_thickness + square_thickness), starting_y, line_thickness, subboard_thickness))
        # Draw Horizontal Lines for Subboard
        pygame.draw.rect(screen, line_color, pygame.Rect(
            starting_x, starting_y + square_thickness + line_count * (line_thickness + square_thickness), subboard_thickness, line_thickness))


def draw_ultimateboard():
    line_color = (0, 0, 0)

    line_thickness = 8
    square_thickness = 168
    subboard_thickness = line_thickness * 2 + square_thickness * 3
    for line_count in range(2):
        # Draw Vertical Lines for Subboard
        pygame.draw.rect(screen, line_color, pygame.Rect(
            square_thickness + line_count * (line_thickness + square_thickness + 4), 0, line_thickness - 3, subboard_thickness))
        # Draw Horizontal Lines for Subboard
        pygame.draw.rect(screen, line_color, pygame.Rect(
            0, square_thickness + line_count * (line_thickness + square_thickness + 4), subboard_thickness, line_thickness - 3))


def draw_X(starting_x, starting_y):
    line_color = (0, 0, 0)
    line_thickness = 5
    pygame.draw.line(screen, line_color, (starting_x + 5, starting_y + 5),
                     (starting_x + 45, starting_y + 45), width=line_thickness)
    pygame.draw.line(screen, line_color, (starting_x + 45,
                     starting_y + 5), (starting_x + 5, starting_y + 45), width=line_thickness)


def draw_O(starting_x, starting_y):
    starting_x += 25
    starting_y += 25
    line_color = (0, 0, 0)
    pygame.draw.circle(screen, line_color,
                       (starting_x, starting_y), 20, width=3)


def mark_square(subboard_coordinates, player):
    sub_row, sub_col = subboard_coordinates
    row = sub_row // 3
    col = sub_col // 3

    sub_row = sub_row - row * 3
    sub_col = sub_col - col * 3

    starting_x = sub_col * 55 + col * 180
    starting_y = sub_row * 55 + row * 180
    if player == "X":
        draw_X(starting_x, starting_y)
    else:
        draw_O(starting_x, starting_y)


def AI_move(current_board_position):
    current_board_square_position, current_board_position = AI.move(
        current_board_position)
    ultimateRow = current_board_position[0] * \
        3 + current_board_square_position[0]
    ultimateCol = current_board_position[1] * \
        3 + current_board_square_position[1]

    mark_square((ultimateRow, ultimateCol), "O")

    board.next_move()

    if board.check_win():
        win_text(board.current_move)

    if board.check_tie():
        tie_text()

    current_board_position = tuple(current_board_square_position)
    sub_board = board.boards[current_board_position[0]
                             ][current_board_position[1]]

    if not board.check_board_availability(sub_board):
        board_chosen = False
        return current_board_position, board_chosen
    board_chosen = True
    current_board_text(current_board_position)
    return current_board_position, board_chosen


def current_board_text(current_board_position):
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = my_font.render(
        f'Current board: {current_board_position}', False, (0, 0, 0))
    screen.blit(text_surface, (width/2 - 90, 555))


def pick_a_board_text():
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = my_font.render(
        'Choose a valid board!', False, (255, 0, 0))
    screen.blit(text_surface, (width/2 - 100, 525))


def win_text(winner):
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = my_font.render(
        f'{winner} Won!', False, (0, 0, 255))
    screen.blit(text_surface, (width/2 - 50, 555))


def tie_text():
    pygame.draw.rect(screen, (255, 255, 255),
                     pygame.Rect(0, 520, 520, 80))
    text_surface = my_font.render(
        'It\'s a Tie!', False, (0, 0, 255))
    screen.blit(text_surface, (width/2 - 100, 555))


while running:

    if board.current_move == "O" and is_AI:
        current_board_position, board_chosen = AI_move(current_board_position)

    width = 520
    height = 520

    x, y = pygame.mouse.get_pos()

    ultimateCol = int
    ultimateRow = int

    for i in range(1, 10):
        if (x < width / 9 * i):
            ultimateCol = i - 1
            break
        else:
            ultimateCol = None

    for i in range(1, 10):
        if (y < height / 9 * i):
            ultimateRow = i - 1
            break
        else:
            ultimateRow = None

    mouse = pygame.mouse.get_pos()

    if not start:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
            width/2 - 250, 540, 100, 50))
        text_surface = my_font.render(
            '1 Player', False, (0, 0, 0))
        screen.blit(text_surface, (width/2 - 240, 555))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
            width/2 + 150, 540, 100, 50))
        text_surface = my_font.render(
            '2 Player', False, (0, 0, 0))
        screen.blit(text_surface, (width/2 + 160, 555))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not start:

            if width/2 - 250 <= mouse[0] <= width/2 - 150 and 540 <= mouse[1] <= 590:
                start = True
                is_AI = True

            if width/2 + 150 <= mouse[0] <= width/2 + 250 and 540 <= mouse[1] <= 590:
                start = True
                is_AI = False

            pygame.draw.rect(screen, (255, 255, 255),
                             pygame.Rect(0, 520, 520, 80))

        if event.type == pygame.MOUSEBUTTONUP and start and not is_won:
            if y > 519:
                break
            elif not first_board_chosen:
                sub_board_position = (ultimateRow // 3, ultimateCol // 3)
                player.choose_board(sub_board_position)
                current_board_position = sub_board_position
                first_board_chosen = True
                board_chosen = True
                current_board_text(current_board_position)

            elif not board_chosen:
                sub_board_position = (ultimateRow // 3, ultimateCol // 3)
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
                sub_board_position = (ultimateRow // 3, ultimateCol // 3)
                if sub_board_position != current_board_position:
                    break
                sub_board_square_row = ultimateRow - (ultimateRow // 3) * 3
                sub_board_square_col = ultimateCol - (ultimateCol // 3) * 3

                sub_board_square_position = (
                    sub_board_square_row, sub_board_square_col)

                try:
                    mark_position = player.move(
                        sub_board_position, sub_board_square_position)
                except ValueError:
                    break

                if board.current_move == "X":
                    mark_square((ultimateRow, ultimateCol), "X")
                else:
                    mark_square((ultimateRow, ultimateCol), "O")
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

        if event.type == pygame.QUIT:
            running = False

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
