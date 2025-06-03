import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    d, t, s = list(map(int, readline().split()))
    print("Yes" if d <= t * s else "No")


if __name__ == '__main__':
    solve()
