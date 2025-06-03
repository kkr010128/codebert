import math
import sys
import os

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")
MOD = 998244353    

# もらうDP(forcus on destination), 区間の和を足しこむ=累積和
N,K = LI()
LRs = [LI() for _ in range(K)]

dp = [0]*(N+1)
cum = [0]*(N+1)
dp[1] = 1
cum[1] = 1
for i in range(2, N+1):
    for j in range(K):
        l, r = LRs[j]
        start = max(0,i-r-1)
        end = max(0,i-l)
        dp[i] += cum[end] - cum[start]
        dp[i] %= MOD
    # 累積和を更新
    cum[i] = (cum[i-1] + dp[i]) % MOD
ans = dp[N]
print(ans)