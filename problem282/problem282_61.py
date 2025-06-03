N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB.sort()
dp = [0] * T
#print("AB:", AB)

answer = 0
for a, b in AB:
  for t in range(T-1, -1, -1):
    if dp[t]:
      if  a + t < T:
        dp[a + t] = max(dp[a + t], dp[t] + b)
        answer = max(answer, dp[a + t])
      else:
        answer = max(answer, dp[t] + b)
  if a < T:
    dp[a] = max(dp[a], b)
  answer = max(answer, b)
  #print("dp:", dp)
print(answer)