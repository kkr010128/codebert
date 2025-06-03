import math
import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    X = int(input())

    lcm = X * 360 // math.gcd(X, 360)
    ans = lcm // X
    print(ans)


if __name__ == "__main__":
    main()
