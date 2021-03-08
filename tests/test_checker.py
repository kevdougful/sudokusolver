import numpy
import pytest
from sudokusolver import Checker, Board

class TestChecker:
    def test_solution_validates(self, easy_solution):
        checker = Checker(board=Board(easy_solution))
        assert checker.is_solved()
