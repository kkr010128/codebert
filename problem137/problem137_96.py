from math import sqrt
itl = lambda: list(map(float, input().strip().split()))


def median(N, C):
    if N % 2:
        return C[N // 2]
    else:
        return C[N // 2 - 1] + C[N // 2]


def solve():
    N = int(input())

    A = []
    B = []
    for _ in range(N):
        a, b = itl()
        A.append(int(a))
        B.append(int(b))
    A.sort()
    B.sort()

    ma = median(N, A)
    mb = median(N, B)
    return mb - ma + 1


if __name__ == '__main__':
    print(solve())