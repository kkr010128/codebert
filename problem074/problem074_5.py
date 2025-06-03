import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N, K = NMI()
    LR = list(sorted([NLI() for _ in range(K)]))
    
    dp = [0 for _ in range(N)]
    dp[0] = 1
    
    cumsum = [0 for _ in range(N+1)]
    cumsum[0] = 0
    cumsum[1] = 1
    
    for n in range(1,N):
        for k in range(K):
            r = n-LR[k][0]
            l = n-LR[k][1]
            if r < 0:
                continue
            else:
                l = max(0,l)
            dp[n] += cumsum[r+1]-cumsum[l]
        dp[n] = dp[n]%MOD2
        cumsum[n+1] = (dp[n] + cumsum[n])%MOD2
    print(dp[-1])
if __name__ == '__main__':
    main()