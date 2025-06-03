import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, M = map(int, input().split())
    ans = N * (N - 1) // 2 + M * (M - 1) // 2
    print(ans)


if __name__ == '__main__':
    solve()
