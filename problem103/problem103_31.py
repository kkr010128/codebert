# DP法でトライ
N = int(input())
A = list(map(int, input().split()))

# i 日目に、株の売却が終了した時点の所持金の最大値
dp = [0]*N
dp[0] = 1000

for i in range(1,N):
    for j in range(0,i):
        dp[i] = max(dp[i], dp[i-1],(dp[j]//A[j])*A[i]+dp[j]%A[j])

print(dp[-1])