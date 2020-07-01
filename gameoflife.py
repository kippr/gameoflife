import math
from expecter import expect


class GameOfLife(object):
    def __init__(self, board):
        size = int(math.sqrt(len(board)))
        assert size * size == len(board), 'Pass a square board please'
        assert set(board).issubset(set('.#')), "Pass board as string of . (dead) and # (alive)"
        self.board = [[int(board[(y * size) + x] == '#')
                       for x in range(size)]
                     for y in range(size)]

    @property
    def size(self):
        return len(self.board)

    def __repr__(self):
        return str(self).replace('\n', '')

    def __str__(self):
        def _cells():
            for row in self.board:
                for cell in row:
                    yield "#" if cell else '.'
                yield "\n"
        return "".join(_cells())



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

expect(str(board("..."
                 "..."
                 "..."))) == "...\n...\n...\n"


print(board("..."
            ".#."
            "..."))
