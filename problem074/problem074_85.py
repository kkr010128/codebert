# import sys
# import math #sqrt,gcd,pi
# import decimal
# import queue # queue
import bisect
# import heapq # priolity-queue
# from time import time
# from itertools import product,permutations,\
    # combinations,combinations_with_replacement
# 重複あり順列、順列、組み合わせ、重複あり組み合わせ
# import collections # deque
# from operator import itemgetter,mul
# from fractions import Fraction
# from functools import reduce

# mod = int(1e9+7)
mod = 998244353
INF = 1<<50

def readInt():
    return list(map(int,input().split()))

def main():
    n,k = readInt()
    l = []
    r = []
    for i in range(k):
        a,b = readInt()
        l.append(a)
        r.append(b)
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dpsum = [0 for i in range(n+1)]
    dpsum[1] = 1
    for i in range(2,n+1):
        for j in range(k):
            lj = max(1,i - r[j])
            rj = i - l[j]
            if rj<1:
                continue
            dp[i] += dpsum[rj] - dpsum[lj-1]
            dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
    print(dp[n])
    return

if __name__=='__main__':
    main()
