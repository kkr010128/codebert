import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    S, T = input().split()
    print(T + S)


if __name__ == '__main__':
    solve()
