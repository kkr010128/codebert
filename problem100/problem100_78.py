import os
import sys
from collections import defaultdict, Counter
from itertools import product, permutations,combinations, accumulate
from operator import itemgetter
from bisect import bisect_left,bisect
from heapq import heappop,heappush,heapify
from math import ceil, floor, sqrt
from copy import deepcopy


def main():
    x = int(input())
    ans = 8
    for i in range(400, 2000, 200):
        if i <= x <= i+199:
            break
        ans -= 1

    print(ans)

if __name__ == '__main__':
	main()
