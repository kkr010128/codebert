from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
input = sys.stdin.readline
INF = float("inf")

MOD = 1000000007

# 処理内容
def main():
    N = int(input())
    
    a = 1
    for _ in range(N):
        a = a * 10 % MOD
    
    b = 1
    for _ in range(N):
        b = b * 9 % MOD
    
    c = 1
    for _ in range(N):
        c = c * 8 % MOD
    
    ans = (a - 2*b + c) % MOD
    print(ans)


if __name__ == '__main__':
    main()