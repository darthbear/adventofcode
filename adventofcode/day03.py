import sys

import itertools

import util


class Day3(object):
    def __init__(self, input_file):
        self._input_file = input_file
        self._moves = self._get_moves()

    def _get_moves(self):
        def get_move(c):
            if c == '>':
                return (1, 0)
            elif c == '<':
                return (-1, 0)
            elif c == '^':
                return (0, -1)
            elif c == 'v':
                return (0, 1)

        with open(self._input_file) as fd:
            return [get_move(c) for c in fd.read() if c in '><^v']

    @staticmethod
    def _add_coords((x1, y1), (x2, y2)):
        return x1 + x2, y1 + y2

    def part1(self):
        all_coords = util.accumulate(self._moves, self._add_coords)
        return len(set(all_coords))

    def part2(self):
        # even moves for santa and odd moves for robo
        santa_moves = self._moves[::2]
        robo_moves = self._moves[1::2]
        santa_coords = util.accumulate(santa_moves, self._add_coords)
        robo_coords = util.accumulate(robo_moves, self._add_coords)
        return len(set(itertools.chain(santa_coords, robo_coords)))


def main():
    input_file = sys.argv[1]
    day3 = Day3(input_file)
    print 'Part1: {solution}'.format(solution=day3.part1())
    print 'Part2: {solution}'.format(solution=day3.part2())


if __name__ == '__main__':
    main()
