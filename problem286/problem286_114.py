import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    A, B = map(int, input().split())

    if 1 <= A and A <= 9 and 1 <= B and B <= 9:
        print(A * B)
    else:
        print('-1')


if __name__ == '__main__':
    solve()
