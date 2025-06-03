import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)



def solve():
    n, t = getList()
    li = []
    for i in range(n):
        li.append(getList())

    li.sort(key=lambda x: 30000 * x[0] + x[1])
    dp = [0] * t
    ans = 0
    for a, b in li:
        tmp = copy.copy(dp)
        ans = max(ans, dp[-1] + b)
        for idx, dd in enumerate(dp):
            # tmp[idx] = max(tmp[idx], dd)
            if idx + a < t:
                tmp[idx + a] = max(dp[idx + a], dp[idx] + b)
        dp = tmp
        for j in range(len(dp) - 1):
            dp[j+1] = max(dp[j], dp[j+1])
    #     print(dp)
    # print(li)
    print(ans)





def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





