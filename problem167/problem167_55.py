import sys
import math


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    r = int(readline())
    print(r * 2 * math.pi)


if __name__ == '__main__':
    solve()
