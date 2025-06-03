import sys

# import bisect
# import numpy as np
# from collections import deque
from collections import deque
# map(int, sys.stdin.read().split())
# import heapq
import bisect


# def input():
#     return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    mod = 10 ** 9 + 7

    if N == K:
        ans = 1
        for i in range(N):
            ans *= A[i]
            ans %= mod
        print(ans % mod)



    elif K % 2 == 0:
        ans = 1
        j = 0
        i = N - 1
        for _ in range(K // 2):
            if A[j] * A[j + 1] > A[i] * A[i - 1]:
                ans *= A[j] * A[j + 1]
                ans %= mod
                j += 2
            else:
                ans *= A[i] * A[i - 1]
                ans %= mod
                i -= 2
        print(ans % mod)

    elif A[-1] < 0:
        ans = 1
        for i in range(K):
            ans *= A[-(i + 1)]
            ans %= mod
        print(ans % mod)
    else:
        ans = A[-1]
        j = 0
        i = N - 2
        for _ in range(K // 2):
            if A[j] * A[j + 1] > A[i] * A[i - 1]:
                ans *= A[j] * A[j + 1]
                ans %= mod
                j += 2
            else:
                ans *= A[i] * A[i - 1]
                ans %= mod
                i -= 2
        print(ans % mod)


if __name__ == "__main__":
    main()
