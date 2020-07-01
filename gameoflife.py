import math
from expecter import expect


class GameOfLife(object):
    def __init__(self, board):
        self.board = board
        self.size = math.sqrt(len(board))
        assert set(board).issubset(set('.#')), "Pass board as string of . (dead) and # (alive)"


def board(board):
    return GameOfLife(board)


expect(board("..."
             "..."
             "...").size) == 3
