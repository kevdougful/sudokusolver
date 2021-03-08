import numpy
from sudokusolver import Solver, Board

class TestSolver:
    def test_returns_solved_array_and_rounds(self, easy):
        solver = Solver(board=Board(cells=easy))
        solution, rounds = solver.solve()
        assert isinstance(solution, numpy.ndarray)
        assert isinstance(rounds, int)

    def test_solves_easy1(self, get_example):
        board, solution = get_example('easy1')
        solver = Solver(board=Board(cells=board))
        answer, rounds = solver.solve()
        assert numpy.all(answer == solution)

    def test_solves_easy2(self, get_example):
        board, solution = get_example('easy2')
        solver = Solver(board=Board(cells=board))
        answer, rounds = solver.solve()
        assert numpy.all(answer == solution)

    def test_solves_medium1(self, get_example):
        board, solution = get_example('medium1')
        solver = Solver(board=Board(cells=board))
        answer, rounds = solver.solve()
        assert numpy.all(answer == solution)

    def test_solves_hard1(self, get_example):
        board, solution = get_example('hard1')
        solver = Solver(board=Board(cells=board))
        answer, rounds = solver.solve()
        assert numpy.all(answer == solution)

    def test_solves_expert1(self, get_example):
        board, solution = get_example('expert1')
        solver = Solver(board=Board(cells=board))
        answer, rounds = solver.solve()
        assert numpy.all(answer == solution)