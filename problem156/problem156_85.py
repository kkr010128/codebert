import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
sys.setrecursionlimit(500*500)
import itertools
from collections import Counter,deque

def main():
    x = int(input())

    for i in range(-120,120):
        for j in range(-120,120):
            if i**5 - j ** 5 == x:
                print(i, j)
                exit()

if __name__=="__main__":
    main()
