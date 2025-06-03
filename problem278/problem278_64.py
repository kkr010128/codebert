import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    r = int(readline())
    print(r * r)


if __name__ == '__main__':
    solve()
