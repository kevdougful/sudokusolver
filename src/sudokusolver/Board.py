import attr
import numpy

from .layouts import layout_9x9


@attr.s(auto_attribs=True)
class Board:
    cells: numpy.array = attr.ib()
    layout: dict = layout_9x9
    values: list = list(range(1, 10))

    def __getitem__(self, loc):
        return self.cells[loc]

    def __setitem__(self, loc, val):
        self.cells[loc] = val

    @cells.validator
    def check_cells(self, attribute, value):
        self.cells = numpy.array(value)

    @staticmethod
    def from_flat(flat):
        arr = numpy.array(list(str(flat)), dtype=numpy.int32).reshape(9, 9)
        return Board(cells=arr)

    def section(self, loc):
        start, end = layout_9x9[loc]
        row_start, col_start = start
        row_end, col_end = end
        return self.cells[row_start:row_end + 1, col_start:col_end + 1]

    def possibilities(self, *loc):
        row, col = loc
        value = self.cells[loc]
        if value > 0:
            return value
        row_values = self.cells[row,]
        col_values = self.cells[:, col]
        section_values = self.section((row, col)).flatten()
        taken = numpy.unique(
            numpy.hstack((row_values, col_values, section_values))
        )
        possible = [i for i in self.values if i not in taken]
        if len(possible) == 1:
            return possible[0]
        else:
            return possible

    def unsolved(self):
        return [
            loc
            for loc in self.layout.keys()
            if self.cells[loc] == 0
        ]
    
    def guess(self):
        guesses = {
            loc: self.possibilities(*loc)
            for loc in self.unsolved()
        }
        solved = {
            loc: value
            for loc, value in guesses.items()
            if not isinstance(value, list)
        }
        board = Board(cells=self.cells[:])
        return board, solved, guesses


