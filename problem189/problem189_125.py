import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    n, m = map(int , input().split())
    print(n*(n-1)//2+m*(m-1)//2)


if __name__=="__main__":
    main()
