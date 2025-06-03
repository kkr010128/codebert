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

    n,t = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    ab.sort(key=lambda x: x[0])
    dp = [-1]*(t+1)
    dp[0] = 0
    for a, b in ab:
        for j in range(t-1, -1, -1):
            if dp[j] >= 0:
                if j+a<=t:
                    dp[j+a] = max(dp[j+a], dp[j]+b)
                else:
                    dp[-1] = max(dp[-1], dp[j]+b)
    print(max(dp))

if __name__ == '__main__':
    main()