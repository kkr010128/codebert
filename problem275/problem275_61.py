# import bisect
# from collections import Counter, defaultdict, deque
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
    x, y = list(map(int,ipti().split()))
    prize = [300000, 200000, 100000, 0]

    if x == y == 1:
        print(1000000)
    else:
        x = 4 if x > 3 else x
        y = 4 if y > 3 else y
        print(prize[x-1]+prize[y-1])

if __name__ == '__main__':
    main()