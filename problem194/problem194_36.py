import itertools,sys
def S(): return sys.stdin.readline().rstrip()
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
H,W = LI()
S = [S() for _ in range(H)]
dp = [[float('INF')]*W for _ in range(H)]
for i,j in itertools.product(range(H),range(W)):
    if i==0:
        if j==0:
            dp[i][j] = 1 if S[i][j]=='#' else 0
        else:
            dp[i][j] = dp[i][j-1]+(1 if S[i][j]=='#' and S[i][j-1]=='.' else 0)
    else:
        if i==0:
            dp[i][j] = dp[i-1][j]+(1 if S[i][j]=='#' and S[i-1][j]=='.' else 0)
        else:
            dp[i][j] = min(dp[i][j],dp[i][j-1]+(1 if S[i][j]=='#' and S[i][j-1]=='.' else 0))
            dp[i][j] = min(dp[i][j],dp[i-1][j]+(1 if S[i][j]=='#' and S[i-1][j]=='.' else 0))
print(dp[-1][-1])
