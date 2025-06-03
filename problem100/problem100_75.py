import math as mt
import sys, string
from collections import Counter, defaultdict
input = sys.stdin.readline

MOD = 1000000007

# input functions
I = lambda : int(input())
M = lambda : map(int, input().split())
Ms = lambda : map(str, input().split()) 
ARR = lambda: list(map(int, input().split()))


def main():
    n = I()
    n -= 400
    print(8 - n//200)

# testcases
tc = 1
for _ in range(tc):
    main()