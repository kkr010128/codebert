import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    a,b,c,d = map(int, input().split())
    while True:
        c -= b
        if c<= 0:
            print("Yes")
            exit()
        a -= d
        if a <= 0:
            print("No")
            exit()

if __name__=="__main__":
    main()
