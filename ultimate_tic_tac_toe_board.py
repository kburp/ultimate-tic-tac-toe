"""
Class representing an ultimate tic-tac-toe board.
"""

from tic_tac_toe_board import TicTacToeBoard


class UltimateTicTacToeBoard:

    def __init__(self):
        self.boards = [[TicTacToeBoard() for i in range(3)] for j in range(3)]
        self._current_move = "X"

    def next_move(self):
        if self.current_move == "X":
            self._current_move = "O"
        else:
            self._current_move = "X"

    def mark_win(self, sub_board):
        for subboard_row in range(0, 3):
            for subboard_column in range(0, 3):
                sub_board.board_state[subboard_row][subboard_column] = ' '
        if self.current_move == 'X':
            sub_board.board_state[0][0] = 'X'
            sub_board.board_state[0][2] = 'X'
            sub_board.board_state[1][1] = 'X'
            sub_board.board_state[2][0] = 'X'
            sub_board.board_state[2][2] = 'X'
            sub_board.win_state = 'X'
        else:
            sub_board.board_state[0][0] = 'O'
            sub_board.board_state[0][1] = 'O'
            sub_board.board_state[0][2] = 'O'
            sub_board.board_state[1][0] = 'O'
            sub_board.board_state[1][2] = 'O'
            sub_board.board_state[2][0] = 'O'
            sub_board.board_state[2][1] = 'O'
            sub_board.board_state[2][2] = 'O'
            sub_board.win_state = 'O'

    def get_board(self, row, col):
        return self.boards[row][col]

    @property
    def current_move(self):
        return self._current_move

    def check_board_availability(self, sub_board):
        if isinstance(sub_board.win_state, str) or sub_board.win_state == 1:
            return False
        return True

    def check_tie(self):
        tie_status = []
        for board_row in self.boards:
            for board in board_row:
                tie_status.append(board.win_state)
        return(0 not in tie_status)

    def check_win(self):
        boards = self.boards
        for i in range(0, 3):
            if boards[i][0].win_state == boards[i][1].win_state == boards[i][2].win_state and isinstance(boards[i][0].win_state, str):
                return boards[i][0].win_state
            if boards[0][i].win_state == boards[1][i].win_state == boards[2][i].win_state and isinstance(boards[0][i].win_state, str):
                return boards[0][i].win_state
        if boards[0][0].win_state == boards[1][1].win_state == boards[2][2].win_state and isinstance(boards[1][1].win_state, str):
            return boards[0][0].win_state
        if boards[0][2].win_state == boards[1][1].win_state == boards[2][0].win_state and isinstance(boards[1][1].win_state, str):
            return boards[0][2].win_state
        return False

    def __repr__(self):
        divider_string = "+-+-+-++-+-+-++-+-+-+\n"
        final_string = ""
        for i in range(3):
            for j in range(3):
                final_string += divider_string + "|"
                for k in range(3):
                    row = self.boards[i][k].board_state[j]
                    final_string += "|".join(row)
                    if k < 2:
                        final_string += "||"
                final_string += "|\n"
            final_string += divider_string
        return final_string
