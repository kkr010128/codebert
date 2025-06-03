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

    x,y = map(int, input().split())
    a = 0
    b = 0
    if x==1:
        a += 300000
    if x==2:
        a += 200000
    if x==3:
        a += 100000
    if y==1:
        b += 300000
    if y==2:
        b += 200000
    if y==3:
        b += 100000
    if a+b == 600000:
        print(1000000)
    else:
        print(a+b)

if __name__ == '__main__':
    main()