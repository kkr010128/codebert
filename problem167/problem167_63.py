import sys
import math


def resolve(in_):
    r = int(in_.read())
    return 2 * r * math.pi


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()