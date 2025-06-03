import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n,k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    if k == 0:
        print(sum(h))
    else:
        h = h[:-k]
        print(sum(h))


if __name__=="__main__":
    main()
