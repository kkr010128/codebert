import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    x = int(input())
    cnt = 0
    a = 100
    while True:
        if a >= x:
            print(cnt)
            exit()
        a = a*101//100
        cnt += 1

if __name__=="__main__":
    main()
