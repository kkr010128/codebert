from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


# 処理内容
def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()[:-1]
    if U == S:
        A -= 1
    else:
        B -= 1
    
    print(A, B)


if __name__ == '__main__':
    main()