import math
from expecter import expect


def _neighbours(board, x, y):
    size = len(board)
    def val(x, y):
        return board[x % size][y % size]
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
        print("\n")
        print(str(self))
        rows = []
        for y, row in enumerate(self.board):
            to_print = ""
            rows.append([])
            for x, cell in enumerate(row):
                neighbours = sum(_neighbours(self.board, x, y))
                to_print = to_print + str(neighbours)
                if cell and neighbours in (2, 3):
                    rows[-1].append(1)
                else:
                    rows[-1].append(0)
            print(to_print)
        next.board = rows
        return next

    def neighbour_count(self, x, y):
        return sum(_neighbours(self.board, x, y))


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

expect(repr(board("..."
                  ".#."
                  "..."))) == ("..."
                               ".#."
                               "...")

expect(board("#.."
             "..#"
             ".#.").neighbour_count(1,1)) == 3


expect(repr(board("..."
                  ".#."
                  "...").next())) == ("..."
                                      "..."
                                      "...")

expect(repr(board(".#."
                  ".#."
                  ".#.").next())) == (".#."
                                      ".#."
                                      ".#.")
expect(repr(board("..."
                  "##."
                  "..#").next())) == ("..."
                                      "##."
                                      "..#")

a = ("...."
     ".##."
     ".##."
     "....")
expect(repr(board(a).next())) == a

b = ("...."
     ".##."
     ".#.."
     "....")
expect(repr(board(b).next())) == b

c = ("##.."
     ".#.."
     ".#.."
     "....")
d = ("#..."
     ".#.."
     ".#.."
     "....")

expect(repr(board(c).next())) == d
