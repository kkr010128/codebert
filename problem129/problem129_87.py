import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    p = [True] * (10**6 + 1)
    s = list(set(a))
    for x in s:
        t = x * 2
        while t <= 10**6:
            p[t] = False
            t += x
    ans = 0
    for x in a:
        if c[x] == 1 and p[x] == True:
            ans += 1
    print(ans)


if __name__=="__main__":
    main()
