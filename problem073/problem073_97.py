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
    n = int(input())
    ans = 0
    for i in range(1,n):
        ans += (n-1)//i

    print(ans)
        

if __name__ == "__main__":
    main()