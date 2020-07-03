import math
from expecter import expect

def _neighbours(board, x, y):
    yield board[x - 1][y - 1]
    yield board[x][y - 1]
    if x + 1 < len(board):
        yield board[x + 1][y - 1]
        yield board[x + 1][y]
        if y + 1 < len(board):
            yield board[x + 1][y + 1]
        else:
            yield board[x + 1][-1]
    else:
        yield board[-1][y - 1]
        yield board[-1][y]
        if y + 1 < len(board):
            yield board[-1][y + 1]
        else:
            yield board[-1][-1]
    yield board[x - 1][y]
    yield board[x - 1][y + 1]
    yield board[x][y + 1]


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
                rows[-1].append(0)
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

expect(repr(board("..."
                  ".#."
                  "...").next())) == ("..."
                                      "..."
                                      "...")

expect(board("#.."
             "..#"
             ".#.").neighbour_count(1,1)) == 3
