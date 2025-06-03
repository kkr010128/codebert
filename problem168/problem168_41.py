import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    print(n - sum(a) if sum(a) <= n else -1)


if __name__ == '__main__':
    solve()
