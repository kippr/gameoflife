import math
from expecter import expect


class GameOfLife(object):
    def __init__(self, board):
        self.board = board
        self.size = int(math.sqrt(len(board)))
        assert set(board).issubset(set('.#')), "Pass board as string of . (dead) and # (alive)"
        self.board = [[1 if board[(y * self.size) + x] == '#' else 0
                       for x in range(self.size)]
                     for y in range(self.size)]


def board(board):
    return GameOfLife(board)


expect(board("..."
             "..."
             "...").size) == 3

expect(board("..."
             "..."
             "...").board) == [[0,0,0], [0,0,0], [0,0,0]]

expect(board("#.."
             ".#."
             "..#").board) == [[1,0,0], [0,1,0], [0,0,1]]
