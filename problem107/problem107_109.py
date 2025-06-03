import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def popcount(n):
    if n == 0:
        return 0
    return 1 + popcount(n % bin(n).count("1"))


def main():
    N = int(input())
    X = input().strip()

    x1 = 0
    xc = bin(int(X, 2)).count("1")
    if xc == 1:
        x2 = -1
    else:
        x2 = 0
    for i in range(N):
        if X[-1 - i] == '1':
            x1 += pow(2, i, xc + 1)
            if x2 != -1:
                x2 += pow(2, i, xc - 1)
    for i in range(N):
        if X[i] == '0':
            print(1 + popcount((x1 + pow(2, N - i - 1, xc + 1)) % (xc + 1)))
        else:
            if x2 == -1:
                print(0)
            else:
                print(1 + popcount((x2 - pow(2, N - i - 1, xc - 1) + xc - 1) % (xc - 1)))


if __name__ == '__main__':
    main()
