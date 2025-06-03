#!/usr/bin/env python3

# from numba import njit

# from collections import Counter
# from itertools import accumulate
# import numpy as np
# from heapq import heappop,heappush
# from bisect import bisect_left

INF = pow(10,6)

# @njit
def solve(n,a):
  res = INF
  for i in range(1,101):
    res = min(res,sum(pow(i-x,2) for x in a))
  return res



def main():
  N = int(input())
  # N,M = map(int,input().split())
  a = list(map(int,input().split()))
  print(solve(N,a))
  return

if __name__ == '__main__':
  main()
