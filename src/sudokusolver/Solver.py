from sudokusolver import Board
import attr
import numpy


@attr.s(auto_attribs=True)
class Solver:
    board: Board
    tries: dict = {}

    def find_new_guess(self):
        pass

    def solve(self, board: Board=None, round=0):
        round += 1
        if board is None:
            board = self.board
        # Take a guess
        new_board, solved, guesses = board.guess()
        # Fill in singles
        for loc, values in solved.items():
            new_board.cells[loc] = values
        if 0 not in new_board.cells:
            return new_board.cells, round
        elif len(solved) > 0:
            # Keep solving
            return self.solve(new_board, round)
        else:
            # Try one of the smaller guesses
            sorted_guesses = sorted(guesses, key=lambda loc: len(guesses.get(loc)))
            if len(self.tries) > 0:
                # Find one we haven't tried yet
                for loc in sorted_guesses:
                    if (numpy.all(numpy.isin(self.tries.keys(), sorted_guesses))):
                        # We tried at least one possibility in each loc
                        # Reset and try from start
                        return self.solve(self.board, round)
                    elif loc in self.tries:
                        # We tried one of the possibilities here, try another
                        guesses_remaining = [
                            t for t in sorted_guesses[loc]
                            if t not in self.tries[loc]
                        ]
                        if len(guesses_remaining) == 0:
                            continue
                        new_board.cells[loc] = guesses_remaining[0]
                        self.tries[loc] = guesses_remaining[0]
                        return self.solve(new_board, round)
            else:
                # Pick the first smallest
                loc = sorted_guesses[0]
                value = guesses[loc][0]
                # Save it in tries
                self.tries[loc] = value
                # Set the value on the board
                new_board.cells[loc] = value
                return self.solve(new_board, round)
                




            