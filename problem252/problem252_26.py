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

    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a)
    c = [0] + sorted(b)
    c = list(accumulate(c))
    a.sort(reverse=True)
    
    # mid以上の和をm個作れるならTrue
    def check(mid):
        total = 0
        for i in a:
            total += n - bisect_left(b, mid-i)
            if total >= m:
                return True
        return False

    l = 0
    r = 2*(10**5)+10
    # 最終的なlがm個以上作れる最小値
    while r - l > 1:
        mid = (l+r) // 2
        if check(mid):
            l = mid
        else:
            r = mid
    res = 0
    for i in a:
        d = bisect_left(b, r-i)
        if d == n:
            continue
        res += i * (n-d) + c[-1] - c[d]
        m -= n - d

    print(res + l*m)

if __name__ == '__main__':
    main()