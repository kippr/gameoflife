import math
from expecter import expect


class GameOfLife(object):
    def __init__(self, board):
        self.board = board
        size = int(math.sqrt(len(board)))
        assert size * size == len(board), 'Pass a square board please'
        assert set(board).issubset(set('.#')), "Pass board as string of . (dead) and # (alive)"
        self.board = [[1 if board[(y * size) + x] == '#' else 0
                       for x in range(size)]
                     for y in range(size)]

    @property
    def size(self):
        return len(self.board)


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
