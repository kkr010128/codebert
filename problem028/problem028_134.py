import sys


def getTheNumberOfCoin(n, m, c):
    T = {}
    for j in range(0, n+1):
        T[j] = 100000
    T[0] = 0

    for i in range(0, m):
        for j in range(c[i], n+1):
            T[j] = min(T[j], T[j-c[i]]+1)

    return T[n]


n, m = (int(x) for x in sys.stdin.readline().split())
c = sorted([int(x) for x in sys.stdin.readline().split()])

print(getTheNumberOfCoin(n, m, c))