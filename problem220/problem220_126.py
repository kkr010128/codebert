import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    if S == U:
        A -= 1
    if T == U:
        B -= 1

    print(A, B)


if __name__ == '__main__':
    solve()
