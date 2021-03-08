import attr
from .Board import Board
import numpy


@attr.s(auto_attribs=True)
class Checker:
    board: Board

    def _valid(self, slice):
        isvalid = True
        flat = slice.flatten()
        uniq = numpy.unique(flat)
        if 0 in slice:
            isvalid = False
        if len(uniq) < len(slice):
            isvalid = False
        return isvalid
    
    def _sections(self):
        centers = [
            (1, 1), (1, 4), (1, 7),
            (4, 1), (4, 4), (4, 7),
            (7, 1), (7, 4), (7, 7),
        ]
        return [self.board.section(loc) for loc in centers]

    def is_solved(self):
        if numpy.any(self.board.cells == 0):
            return False
        elif not any([self._valid(self.board[row, ]) for row in range(0, 9)]):
            return False
        elif not any([self._valid(self.board[:, col]) for col in range(0, 9)]):
            return False
        elif not any([self._valid(section) for section in self._sections()]):
            return False
        else:
            return True
