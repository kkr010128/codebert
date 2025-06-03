import sys
import numpy as np

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    cumsum = np.cumsum(A)
    half = sum(A) // 2

    ans = INF
    for i in range(N - 1):
        left = cumsum[i]
        right = cumsum[-1] - cumsum[i]
        cost = abs(half - left) + abs(right - half)
        if cost < ans:
            ans = cost

    print(ans)


if __name__ == "__main__":
    main()
