import sys
import bisect
import itertools
import collections
import fractions
import heapq
import math
from operator import mul
from functools import reduce
from functools import lru_cache


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    N, T = map(int, readline().split())
    dishes = []
    for _ in range(N):
        A, B = map(int, readline().split())
        dishes.append([A, B])

    dp1 = [[0]*T for _ in range(N)] # i and less than i
    dp2 = [[0]*T for _ in range(N+1)] # more than i

    for i, dish in enumerate(dishes[:-1]):
        a, b = dish
        i = i + 1
        for t in range(T):
            if a > t:
                dp1[i][t] = dp1[i-1][t]
            else:
                if dp1[i-1][t-a] + b > dp1[i-1][t]:
                    dp1[i][t] = dp1[i-1][t-a] + b
                else:
                    dp1[i][t] = dp1[i-1][t]


    for i, dish in enumerate(reversed(dishes[1:])):
        a, b = dish
        i = N - i - 1
        for t in range(T):
            if a > t:
                dp2[i][t] = dp2[i+1][t]
            else:
                if dp2[i+1][t-a] + b > dp2[i+1][t]:
                    dp2[i][t] = dp2[i+1][t-a] + b
                else:
                    dp2[i][t] = dp2[i+1][t]

    ans = 0
    for last in range(1, N+1):
        for j in range(T):
            a = dishes[last-1][1]
            a += dp1[last-1][T-1-j] + dp2[last][j]
            ans = a if ans < a else ans
    print(ans)


if __name__ == '__main__':
    solve()