import math
from itertools import islice
from expecter import expect


def _neighbours(board, x, y):
    size = len(board)
    def val(x, y):
        return board[y % size][x % size]
    yield val(x - 1, y - 1)
    yield val(x, y - 1)
    yield val(x + 1, y - 1)
    yield val(x - 1, y)
    yield val(x + 1, y)
    yield val(x - 1, y + 1)
    yield val(x, y + 1)
    yield val(x + 1, y + 1)


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

    def next(self):
        next = GameOfLife("")
        rows = []
        for y, row in enumerate(self.board):
            rows.append([])
            for x, cell in enumerate(row):
                neighbours = sum(_neighbours(self.board, x, y))
                if cell:
                    if neighbours in (2, 3):
                        rows[-1].append(1)
                    else:
                        rows[-1].append(0)
                else:
                    rows[-1].append(int(neighbours == 3))
        next.board = rows
        return next

    def __iter__(self):
        board = self
        while True:
            yield board
            board = board.next()


def board(board):
    return GameOfLife(board)


expect(str(board("..."

                 "..."
                 "..."))) == "...\n...\n...\n"


expect(repr(board("..."
                  ".#."
                  "..."))) == ("..."
                               ".#."
                               "...")


expect(repr(board("..."
                  ".#."
                  "...").next())) == ("..."
                                      "..."
                                      "...")


a = ("...."
     ".##."
     ".##."
     "....")
expect(repr(board(a).next())) == a


c = ("##.."
     ".#.."
     ".#.."
     "....")
d = ("##.."
     ".##."
     "...."
     "##..")
expect(repr(board(c).next())) == d

v = ("....."
     "..#.."
     "..#.."
     "..#.."
     ".....")

h = ("....."
     "....."
     ".###."
     "....."
     ".....")

expect([repr(b) for b in islice(iter(board(v)), 4)]) == [v,h,v,h]
