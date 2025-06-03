import sys

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 19
MOD = 998244353

N, K = MAP()
A = LIST()

dp = list2d(N+1, K+1, 0)
dp[0][0] = 1
for i, a in enumerate(A):
    for j in range(K+1):
        dp[i+1][j] += dp[i][j] * 2
        dp[i+1][j] %= MOD
        if j+a <= K:
            dp[i+1][j+a] += dp[i][j]
            dp[i+1][j+a] %= MOD
ans = dp[N][K]
print(ans)
