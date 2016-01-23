import sys


def main():
    input_file = sys.argv[1]
    with open(input_file) as fd:
        content = fd.read()
        moves = (1 if c == '(' else -1 for c in content if c in '()')
        floor = sum(moves)
        print floor


if __name__ == '__main__':
    main()
