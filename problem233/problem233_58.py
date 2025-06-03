import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = p[0]
    cnt = 0
    for i in p:
        if i <= min:
            cnt += 1
            min = i
        else:
            pass
    print(cnt)


if __name__=="__main__":
    main()
