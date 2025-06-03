import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    a = int(readline())
    print(a + a ** 2 + a ** 3)


if __name__ == '__main__':
    solve()
