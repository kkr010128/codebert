import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    H, A = map(int, input().split())

    q, r = divmod(H, A)
    if r > 0:
        q = q + 1
    print(q)


if __name__ == '__main__':
    solve()
