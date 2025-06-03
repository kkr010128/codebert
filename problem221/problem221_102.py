import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    n = len(input())
    ans = 'x' * n
    print(ans)


if __name__ == '__main__':
    solve()
