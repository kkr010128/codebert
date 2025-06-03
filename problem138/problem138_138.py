MOD = 998244353

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, S = ZZ()
    A = ZZ()
    dp = [[0] * (S+1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S+1):
            dp[i+1][j] += 2*dp[i][j]
            if A[i] <= j <= S: dp[i+1][j] += dp[i][j-A[i]]
            dp[i+1][j] %= MOD
    print(dp[N][S])

    return

if __name__ == '__main__':
    main()
