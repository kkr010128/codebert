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

    #inf = 10**17
    #mod = 10**9 + 7

    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    f =list(map(int, input().split()))
    a.sort()
    f.sort(reverse=True)

    def check(mid, k):
        for i in range(n):
            if a[i]*f[i] <= mid:
                continue
            k -= a[i] - mid // f[i]
            if k < 0:
                return False
        return True

    ng = -1
    ok = 10**12
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid, k):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()