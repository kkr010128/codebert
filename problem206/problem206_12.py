import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    ans = int(N / 2 + 0.6)
    print(ans)


if __name__ == '__main__':
    solve()
