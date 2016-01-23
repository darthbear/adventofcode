import sys

import util


class Day1(object):
    def __init__(self, input_file):
        self._input_file = input_file

    def _get_moves(self):
        """return iterator +1 for floor up and -1 for floor down"""
        with open(self._input_file) as fd:
            content = fd.read()
            return (1 if c == '(' else -1 for c in content if c in '()')

    def part1(self):
        moves = self._get_moves()
        final_floor = sum(moves)
        return final_floor
        print 'Part1: {response}'.format(response=final_floor)

    def part2(self):
        moves = self._get_moves()
        floors = util.accumulate(moves)
        position = next((pos for pos, f in enumerate(floors) if f == -1), None)
        return position
        print 'Part2: {response}'.format(response=position)


def main():
    input_file = sys.argv[1]
    day1 = Day1(input_file)
    print 'Part1: {solution}'.format(solution=day1.part1())
    print 'Part2: {solution}'.format(solution=day1.part2())


if __name__ == '__main__':
    main()
