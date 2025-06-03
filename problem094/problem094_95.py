import sys
input = sys.stdin.readline
def main():
    R, C,K = map(int, input().split())
    dp = [[[0]*(C+1) for k in range(R+1)] for _ in range(4)]
    # dp[r][c][j] :=r index c columns already j cnt
    dp[0][0][0] = 0
    D = [[0 for i in range(C+1)] for j in range(R+1)]
    import random
    for i in range(K):
        r, c, v = map(int,input().split())
        D[r][c] = v
    
    for i in range(R+1):
        for j in range(C+1):
            if D[i][j] > 0:
                v = D[i][j]
                M = max(dp[k][i-1][j] for k in range(4))
                dp[0][i][j] = max(dp[0][i][j-1], M)
                dp[1][i][j] = max(dp[0][i][j-1]+v, dp[1][i][j-1], M+v)
                dp[2][i][j] = max(dp[1][i][j-1]+v, dp[2][i][j-1])
                dp[3][i][j] = max(dp[2][i][j-1]+v, dp[3][i][j-1])
    
            else:
                M = max(dp[k][i-1][j] for k in range(4))
                dp[0][i][j] = max(dp[0][i][j-1], M)
                dp[1][i][j] = dp[1][i][j-1]
                dp[2][i][j] = dp[2][i][j-1]
                dp[3][i][j] = dp[3][i][j-1]
    
    
    ans = max(dp[i][-1][-1] for i in range(4))
    print(ans)
main()