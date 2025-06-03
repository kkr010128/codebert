

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    a,b,c,d,e = map(int, input().split())
    if d >= b:
        res = (c-a)*60 + d-b
        print(res-e)
    else:
        res = (c-a-1)*60 + d-b+60
        print(res-e)

if __name__ == '__main__':
    main()