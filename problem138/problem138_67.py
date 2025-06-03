import sys
sys.setrecursionlimit(10000000)
MOD = 998244353
INF = 10 ** 15

def main():
    N,S = map(int,input().split())
    A = list(map(int,input().split()))

    dp = [[0]*(1 + S) for _ in range(N + 1)]
    dp[0][0] = pow(2,N,MOD)
    inv2 = pow(2,MOD - 2,MOD)
    for i,a in enumerate(A):
        for j in range(S + 1):
            if j < a:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = (dp[i][j] + dp[i][j - a] * inv2)%MOD
    print(dp[N][S])
if __name__ == '__main__':
    main()