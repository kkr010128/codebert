N = input()
n = len(N)
dp = [[0,0]for i in range(0,n,1)]#[i][0]その桁はピッタリ払う[i][1]一つ上の桁を１枚つかう　ときの合計枚数

dp[n-1][0] = int(N[n-1])
dp[n-1][1] = int(10 - int(N[n-1]) + 1 )#一つ上の桁で払うandおつり

for i in range(n-2,-1,-1):
    dp[i][0] = int(N[i]) + min(dp[i+1][0],dp[i+1][1])
    dp[i][1] = 10 - int(N[i]) + 1 + min(dp[i+1][0],dp[i+1][1] - 2)#次の桁で払った、の＋１を取り消すマイナス１と繰り下がりの

print(min(dp[0][0],dp[0][1]))