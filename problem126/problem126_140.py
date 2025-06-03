import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    x = list(map(int, readline().split()))
    print(x.index(0) + 1)


if __name__ == '__main__':
    solve()
