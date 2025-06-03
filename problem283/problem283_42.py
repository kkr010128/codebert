import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    cnt = 0
    for i in range(1, n):
        if i + 1 <= n - i <= n:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
