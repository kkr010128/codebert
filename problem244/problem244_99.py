import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    k, x = list(map(int, readline().split()))
    print("Yes" if 500 * k >= x else "No")


if __name__ == '__main__':
    solve()
