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
    a, b, c = M()
    k = I()
    ans = 0
    while b <= a:
        b *= 2
        ans += 1
    while c <= b:
        c *= 2
        ans += 1
    if ans <= k:
        print("Yes")
    else:
        print("No")

# testcases
tc = 1
for _ in range(tc):
    main()