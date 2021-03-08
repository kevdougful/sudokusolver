import numpy
import pytest

@pytest.fixture
def examples():
    return {
        'easy1': {
            'board': '000260701680070090190004500820100040004602900050003028009300074040050036703018000',
            'solution': '435269781682571493197834562826195347374682915951743628519326874248957136763418259',
        },
        'easy2': {
            # https://www.memory-improvement-tips.com/printable-sudoku-puzzles-easy-1b.html
            'board': '096040030057820000100900500009010008500000002400090600004003001000079260020050980',
            'solution': '296145837357826149148937526639512478581764392472398615964283751815479263723651984',
        },
        'medium1': {
            # https://www.memory-improvement-tips.com/printable-sudoku-puzzles-medium-1b.html
            'board': '108006400006090807500000000269500080000409000080002791000000005604070200001200903',
            'solution': '198756432326194857547328169269517384713489526485632791932841675654973218871265943',
        },
        'hard1': {
            # https://www.memory-improvement-tips.com/printable-sudoku-puzzles-hard-1b.html
            'board': '000000806405690010009002400500003080007809600090200003004700100060041708703000000',
            'solution': '231574896475698312689132475526413987347859621198267543854726139962341758713985264',
        },
        'expert1': {
            # https://www.memory-improvement-tips.com/printable-sudoku-puzzles-very-hard-1b.html
            'board': '960040100000380000708060009120800903000050000305002064800090407000038000009020085',
            'solution': '962745138541389276738261549126874953497653812385912764853196427274538691619427385',
        },
    }

@pytest.fixture
def get_example(examples):
    from_flat = lambda s: numpy.array(
        list(str(s)), dtype=numpy.int32
    ).reshape(9, 9)
    def func(difficulty):
        example = examples.get(difficulty)
        board = from_flat(example.get('board'))
        solution = from_flat(example.get('solution'))
        return board, solution
    return func

@pytest.fixture
def easy():
    return [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0],
    ]


@pytest.fixture
def easy_section_1():
    return numpy.array([
        [0, 0, 0],
        [6, 8, 0],
        [1, 9, 0]
    ])


@pytest.fixture
def easy_solution():
    return [
        [4, 3, 5, 2, 6, 9, 7, 8, 1],
        [6, 8, 2, 5, 7, 1, 4, 9, 3],
        [1, 9, 7, 8, 3, 4, 5, 6, 2],
        [8, 2, 6, 1, 9, 5, 3, 4, 7],
        [3, 7, 4, 6, 8, 2, 9, 1, 5],
        [9, 5, 1, 7, 4, 3, 6, 2, 8],
        [5, 1, 9, 3, 2, 6, 8, 7, 4],
        [2, 4, 8, 9, 5, 7, 1, 3, 6],
        [7, 6, 3, 4, 1, 8, 2, 5, 9],
    ]


@pytest.fixture
def cells_empty_valid():
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]


@pytest.fixture
def cells_empty_invalid():
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]


@pytest.fixture
def cells_filled_valid():
    return [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16],
    ]


@pytest.fixture
def cells_non_numeric():
    return [
        ['a', 'b', 'c', 'd'],
        ['a', 'b', 'c', 'd'],
        ['a', 'b', 'c', 'd'],
        ['a', 'b', 'c', 'd'],
    ]

@pytest.fixture
def expert_flat():
    return '900672000200001400000000008000100000740390080006004000000000029000000001561000700'

@pytest.fixture
def expert():
    return numpy.array([
        [9, 0, 0, 6, 7, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 1, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [7, 4, 0, 3, 9, 0, 0, 8, 0],
        [0, 0, 6, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [5, 6, 1, 0, 0, 0, 7, 0, 0]
    ])