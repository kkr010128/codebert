import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    n = int(input())
    l = list(map(int, input().split()))
    ans = INF
    for i in range(1,101):
        trial = 0
        for k in l:
            trial += (k-i)**2
        ans = min(ans, trial)
    print(ans)

if __name__=="__main__":
    main()
