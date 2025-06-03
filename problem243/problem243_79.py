# import bisect
# from collections import Counter, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
# import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    n = int(input())

    s = [0] * n
    t = [0] * n

    for i in range(n):
        s[i], t[i] = input().split()
        t[i] = int(t[i])

    x = input()

    idx = s.index(x)
    ans = 0

    for i in range(idx+1, n):
        ans += t[i]

    print(ans)



if __name__ == '__main__':
    main()