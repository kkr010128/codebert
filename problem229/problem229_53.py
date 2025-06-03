H, N = list(map(int,input().split()))
A = []
B = []
for i in range(N):
    in1, in2 = list(map(int,input().split()))
    A.append(in1)
    B.append(in2)
    
# dp[i]: モンスターの体力がiのときの最適値
INF = 10 ** 9 + 7
dp = [INF for _ in range(H + 1)]
dp[0] = 0

for i in range(1, H + 1):
    for j in range(N):
        dp[i] = min(dp[i], dp[max(0, i - A[j])] + B[j])
        
print(dp[H])