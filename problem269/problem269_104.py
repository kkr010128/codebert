import sys
from math import gcd


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())

    P = (A1 - B1) * T1
    Q = (A2 - B2) * T2

    if P > 0:
        P = P * (-1)
        Q = Q * (-1)

    if P + Q < 0:
        print(0)
        return
    elif P + Q == 0:
        print("infinity")
        return
    else:
        S = (-P) // (P + Q)
        T = (-P) % (P + Q)
        if T == 0:
            print(2 * S)
        else:
            print(2 * S + 1)


if __name__ == "__main__":
    main()
