from expecter import expect


class GameOfLife(object):
    def __init__(self, board):
        self.board = board

    @property
    def size(self):
        return 3

def board(board):
    return GameOfLife(board)


expect(board("..."
             "..."
             "...").size) == 3
