"""何回でも同じ荷物を選べるナップザック問題"""
def main():
    H,N = map(int, input().split())
    A,B = [],[]
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    # dp[i][j] = i種類の魔法から、合計ダメージがj以上となるような魔力の最小値
    INF = float('inf')
    dp = [[INF]*(H+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1,N+1):
        for j in range(H+1):
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j-A[i-1]>=0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-A[i-1]]+B[i-1])
                dp[i][j] = min(dp[i][j], dp[i][j-A[i-1]]+B[i-1])
            else:
                dp[i][j] = min(dp[i][j], B[i-1])
    print(dp[N][H])

main()
