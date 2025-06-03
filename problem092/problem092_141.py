import sys


def input():
    return sys.stdin.readline().rstrip('\n')


def calc(X, K, D):
    X = abs(X)
    n = X // D
    if K <= n:
        return abs(X - K * D)
    if (K - n) % 2 == 0:
        return abs(X - n * D)
    else:
        return abs(X - (n + 1) * D)


(X, K, D) = tuple([int(s) for s in input().split()])
print(calc(X, K, D))