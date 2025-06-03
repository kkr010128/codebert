# 0や1のケースに注意
# index out of range
# 貪欲

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

    t = input().rstrip()
    res = []
    for i in range(len(t)):
        if t[i] != '?':
            res.append(t[i])
        else:
            res.append('D')
    print(''.join(res))

if __name__ == '__main__':
    main()