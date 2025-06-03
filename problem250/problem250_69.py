import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    x = int(input())
    while True:
        if all( x%i != 0 for i in range(2,x)):
            print(x)
            exit()
        x += 1

if __name__=="__main__":
    main()
