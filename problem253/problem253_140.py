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

    n,a,b = map(int, input().split())
    if (b-a) % 2 == 0:
        print((b-a)//2)
    else:
        if b-a == 1:
            print(min(b-1, n-a))
        else:
            print(min(a-1+(b-a+1)//2, n-b+(b-a+1)//2))

if __name__ == '__main__':
    main()