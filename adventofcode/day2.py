import sys


class Day2(object):
    def __init__(self, input_file):
        self._input_file = input_file

    def _get_dimensions(self):
        with open(self._input_file) as fd:
            for line in fd:
                dimension = [int(d) for d in line.strip().split('x')]
                yield dimension

    def part1(self):
        def get_surface(l, w, h):
            side1 = l * w
            side2 = w * h
            side3 = h * l
            return 2 * l * w + 2 * w * h + 2 * h * l + min(side1, side2, side3)

        dimensions = self._get_dimensions()
        total_surface = sum((get_surface(*dimension) for dimension in dimensions))
        return total_surface

    def part2(self):
        def get_ribbon_surface(l, w, h):
            # 2 min dimensions
            m1, m2 = sorted([l, w, h])[:2]
            return 2 * (m1 + m2) + l * w * h

        dimensions = self._get_dimensions()
        total_ribbon = sum((get_ribbon_surface(*dimension) for dimension in dimensions))
        return total_ribbon


def main():
    input_file = sys.argv[1]
    day2 = Day2(input_file)
    print 'Part1: {solution}'.format(solution=day2.part1())
    print 'Part2: {solution}'.format(solution=day2.part2())


if __name__ == '__main__':
    main()
