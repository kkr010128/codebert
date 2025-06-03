import math


def solve():
    N = int(input())
    if math.floor(math.ceil(N / 1.08) * 1.08) == N:
        print(math.ceil(N / 1.08))
    else:
        print(':(')


if __name__ == "__main__":
    solve()