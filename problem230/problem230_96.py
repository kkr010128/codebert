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

    n,d,a = map(int, input().split())
    xh = [list(map(int, input().split())) for _ in range(n)]
    xh.sort(key=lambda a: a[0])
    x = []
    for i in range(n):
        x.append(xh[i][0])
    res = 0
    hp = [0]*n
    for i in range(n):
        if i != 0:
            hp[i] += hp[i-1]
        if hp[i]>=xh[i][1]:
            continue
        res += (xh[i][1]-hp[i]-1) // a + 1
        attack = ((xh[i][1]-hp[i]-1) // a + 1) * a
        hp[i] += attack
        genkai = x[i] + 2 * d
        migi = bisect_right(x, genkai)
        if migi <= n - 1:
            hp[migi] -= attack

    print(res)

if __name__ == '__main__':
    main()