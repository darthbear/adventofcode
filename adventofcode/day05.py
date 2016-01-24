import sys

import itertools

import util


class Day5(object):
    VOWELS = 'aeiou'
    DISALLOWED_SUBSTRINGS = ['ab', 'cd', 'pq', 'xy']

    def __init__(self, input_file):
        self._input_file = input_file

    def _get_strings(self):
        """return iterator +1 for floor up and -1 for floor down"""
        with open(self._input_file) as fd:
            for line in fd:
                yield line

    def _has_3_vowels(self, s):
        return len([c for c in s if c in self.VOWELS]) >= 3

    @staticmethod
    def _has_double_letters(s):
        return any((True for a, b in util.slide(2, s) if a == b))

    @classmethod
    def _has_disallowed_substrings(cls, s):
        return any((True for d in cls.DISALLOWED_SUBSTRINGS if d in s))

    def _is_nice(self, s):
        return self._has_3_vowels(s) \
               and self._has_double_letters(s) \
               and not self._has_disallowed_substrings(s)

    def part1(self):
        return sum((1 for line in self._get_strings() if self._is_nice(line)))

    @staticmethod
    def _has_double_couples(s):
        couples = util.slide(2, s)
        couple_groups = [
            list(value)
            for key, value
            in itertools.groupby(
                    sorted(
                            enumerate(couples),
                            key=lambda (_, letters): letters
                    ),
                    key=lambda (_, letters): letters
            )
            ]

        couple_groups_pos_with_dupes = [[pos for pos, _ in groups] for groups in couple_groups if len(groups) > 1]

        def no_overlap(iterable):
            sorted_list = sorted(iterable)
            return sorted_list[-1] - sorted_list[0] > 1

        return any([no_overlap(same_couples) for same_couples in couple_groups_pos_with_dupes])

    @staticmethod
    def _has_double_letters_with_middle(s):
        return any([True for a, _, c in  util.slide(3, s) if a == c])

    def part2(self):
        return sum([1 for line in self._get_strings() if self._has_double_couples(line) and self._has_double_letters_with_middle(line)])


def main():
    input_file = sys.argv[1]
    day5 = Day5(input_file)
    print 'Part1: {solution}'.format(solution=day5.part1())
    print 'Part2: {solution}'.format(solution=day5.part2())


if __name__ == '__main__':
    main()
