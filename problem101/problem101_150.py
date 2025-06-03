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
    a,b,c = map(int, input().split())
    k = int(input())
    flag = False
    if a < b < c:
        print("Yes")
        sys.exit()

    for i in range(k):
        if a < b < c:
            c *= 2
        if a >= b:
            if b >= c:
                c *= 2
            else:
                b *= 2
        else:
            if b >= c:
                c *= 2
            else:
                b *= 2

    if a < b < c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
	main()
