import numpy
import pytest

from sudokusolver import Board


class TestBoard:
    def test_board_instantiates(self, get_example):
        easy, _ = get_example('easy1')
        assert Board(cells=easy)

    def test_returns_correct_section(self, easy, easy_section_1):
        assert numpy.all(Board(cells=easy).section((1, 1)) == easy_section_1)

    def test_generates_board_from_string(self, expert, expert_flat):
        board = Board.from_flat(expert_flat)
        assert isinstance(board, Board)
        assert numpy.all(board.cells == expert)

    def test_unsolved_returns_array_of_locs(self, easy):
        board = Board(cells=easy)
        unsolveds = board.unsolved()
        assert isinstance(unsolveds, list)
        assert all([isinstance(u, tuple) for u in unsolveds])
    
    def test_finds_unsolveds(self, easy_solution):
        board = Board(cells=easy_solution)
        loc = (4, 4)
        board[loc] = 0
        unsolveds = board.unsolved()
        assert len(unsolveds) == 1
        assert unsolveds[0] == loc


