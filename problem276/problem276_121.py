def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    a =[0]+list(map(int, input().split()))
    b = list(accumulate(a))
    c = sum(a)
    res = 10000000000000000
    for i in range(1, n):
        s = b[i]
        t = c-s
        res = min(res, abs(s-t))
    print(res)


if __name__ == '__main__':
    main()