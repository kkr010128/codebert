import sys

# import re
# import math
# import collections
# import decimal
# import bisect
# import itertools
# import fractions
# import functools
# import copy
# import heapq
# import decimal
# import statistics
# import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 10
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    mat = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(1, n + 1):
        s = str(i)
        ss = int(s[0])
        st = int(s[-1])
        mat[ss][st] += 1

    ans=0
    for i in range(1,10):
        for j in range(1,10):
            ans += mat[i][j]*mat[j][i]

    print(ans)




if __name__ == '__main__':
    main()
