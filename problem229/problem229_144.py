H, N = map(int, input().split())

A = []
B = []

for n in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
  
INF = float('inf')
dp = [INF] * (H + max(A))
dp[0] = 0
# dp[i]を、HP iを減らすために必要な最小の魔力とする

for hp in range(1, H+1):
  for n in range(N):
      dp[hp] = min(dp[max(hp-A[n],0)] + B[n], dp[hp])

print(dp[H])