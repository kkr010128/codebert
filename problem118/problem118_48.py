import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    ans = 0
    n = int(input())
    for j in range(1,n+1):
        ans += j*(n//j)*(n//j + 1)//2
    print(ans)

if __name__=="__main__":
    main()
