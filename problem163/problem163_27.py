#MLE注意！0や1のケースに注意

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    s,w = map(int, input().split())
    if s<=w:
        print('unsafe')
    else:
        print('safe')

if __name__ == '__main__':
    main()