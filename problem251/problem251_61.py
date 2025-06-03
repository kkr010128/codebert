# import sys
# import math #sqrt,gcd,pi
# import decimal
# import queue # queue
# import bisect
# import heapq # priolity-queue
# import time
# from itertools import product,permutations,\
#     combinations,combinations_with_replacement
# 重複あり順列、順列、組み合わせ、重複あり組み合わせ
# import collections # deque
# from operator import itemgetter,mul
# from fractions import Fraction
# from functools import reduce

mod = int(1e9+7)
# mod = 998244353
INF = 1<<50

def readInt():
    return list(map(int,input().split()))

def main():
    n,k = readInt()
    r,s,p = readInt()
    rsp = {"s":r,"p":s,"r":p}
    t = input()
    ans = 0
    u = []
    for i in range(n):
        if i<k:
            ans += rsp[t[i]]
            u.append(t[i])
        else:
            if t[i]!=u[i-k]:
                ans += rsp[t[i]]
                u.append(t[i])
            else:
                u.append("f")
    print(ans)
    return

if __name__=='__main__':
    main()
