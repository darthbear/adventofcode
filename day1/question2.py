import sys
import operator


#
# Backport of itertools.accumulate from Python 3
#

def accumulate(iterable, func=operator.add):
    """Return running totals"""
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


def main():
    input_file = sys.argv[1]
    with open(input_file) as fd:
        content = fd.read()

        moves = (1 if c == '(' else -1 for c in content if c in '()')
        floors = accumulate(moves)
        position = next((pos for pos, f in enumerate(floors) if f == -1), None)
        print position + 1


if __name__ == '__main__':
    main()
