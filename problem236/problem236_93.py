# import bisect
from collections import Counter, defaultdict, deque
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
import math

import sys

# import numpy as np

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    h, w, n = map(int, open(0).read().split())

    print(math.ceil(n/max(h, w)))

if __name__ == '__main__':
    main()