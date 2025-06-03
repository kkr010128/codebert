import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    n, r = map(int,input().split())
    if 10 > n:
        print(r + (100 * (10 - n)))
    else:
        print(r)


if __name__ == '__main__':
    solve()
