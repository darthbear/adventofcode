import functools
import sys

from collections import namedtuple

import util

XY = namedtuple('XY', ['x', 'y'])
Toggle = namedtuple('Toggle', ['pos1', 'pos2'])
Turn = namedtuple('Turn', ['status', 'pos1', 'pos2'])


class Day6(object):
    def __init__(self, input_file):
        self._instructions = self._get_instructions(input_file)

    def _get_instructions(self, input_file):
        def parse_xy(xy):
            return XY(*[int(i) for i in xy.split(',')])

        def parse_instruction(s):
            tokens = s.split(' ')
            if tokens[0] == 'toggle':
                return Toggle(parse_xy(tokens[1]), parse_xy(tokens[3]))
            else:
                return Turn(tokens[1], parse_xy(tokens[2]), parse_xy(tokens[4]))

        """return iterator +1 for floor up and -1 for floor down"""
        with open(input_file) as fd:
            return [parse_instruction(line) for line in fd]

    def part1(self):
        def create_lights(pos1, pos2):
            return set([XY(x, y) for x in range(pos1.x, pos2.x + 1) for y in range(pos1.y, pos2.y + 1)])

        def toggle(onlights, pos1, pos2):
            turned_off_lights, turned_on_lights = util.partition(
                    lambda light: light in onlights,
                    create_lights(pos1, pos2)
            )
            return onlights.difference(turned_on_lights).union(turned_off_lights)

        def turn(onlights, pos1, pos2, status):
            lights_to_turn = create_lights(pos1, pos2)

            if status == 'on':
                return onlights.union(lights_to_turn)
            else:
                return onlights.difference(lights_to_turn)

        def play(onlights, instruction):
            if isinstance(instruction, Toggle):
                return toggle(onlights, instruction.pos1, instruction.pos2)
            else:
                return turn(onlights, instruction.pos1, instruction.pos2, instruction.status)

        lights = functools.reduce(play, self._instructions, set())
        return len(lights)

    def part2(self):

        def create_lights(pos1, pos2):
            return set([XY(x, y) for x in range(pos1.x, pos2.x + 1) for y in range(pos1.y, pos2.y + 1)])

        def toggle(onlights, pos1, pos2):
            new_lights = [(xy, onlights.get(xy, 0) + 2) for xy in create_lights(pos1, pos2)]
            return dict(onlights.items() + new_lights)

        def turn(onlights, pos1, pos2, status):
            new_lights = create_lights(pos1, pos2)

            if status == 'on':
                lights_to_turn_on = [(xy, onlights.get(xy, 0) + 1) for xy in new_lights]
                return dict(onlights.items() + lights_to_turn_on)
            else:
                lights_with_neg = ((xy, v - (1 if xy in new_lights else 0)) for xy, v in onlights.items())
                return {xy: v for xy, v in lights_with_neg if v > 0}

        def play(onlights, instruction):
            if isinstance(instruction, Toggle):
                return toggle(onlights, instruction.pos1, instruction.pos2)
            else:
                return turn(onlights, instruction.pos1, instruction.pos2, instruction.status)

        lights = functools.reduce(play, self._instructions, {})
        return sum(lights.values())


def main():
    input_file = sys.argv[1]
    day6 = Day6(input_file)
    print 'Part1: {solution}'.format(solution=day6.part1())
    print 'Part2: {solution}'.format(solution=day6.part2())


if __name__ == '__main__':
    main()
