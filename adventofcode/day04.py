import hashlib

import sys


class Day4(object):
    MAX_NUM = 10000000

    def __init__(self, input_file):
        with open(input_file) as fd:
            self._prefix = fd.read()

    @staticmethod
    def _md5(s):
        h = hashlib.md5()
        h.update(s)
        return h.hexdigest()

    def solve(self, num_start_zeroes):
        zeroes = '0' * num_start_zeroes
        return next((i for i, s in (
            (i, self._md5(self._prefix + str(i))) for i in range(self.MAX_NUM)) if s.startswith(zeroes)
                     ), None
                    )

    def part1(self):
        return self.solve(5)

    def part2(self):
        return self.solve(6)


def main():
    input_file = sys.argv[1]
    day4 = Day4(input_file)
    print 'Part1: {solution}'.format(solution=day4.part1())
    print 'Part2: {solution}'.format(solution=day4.part2())


if __name__ == '__main__':
    main()
