N, P = map(int, input().split())
S = input()

if P in [2, 5]:
  ans = 0
  for i, s in enumerate(S, 1):
    if int(s) % P == 0:
      ans += i
  print(ans)
else:
  dp = [0] * (N+1)
  for i, s in enumerate(S, 1):
    dp[i] = (dp[i-1]*10 + int(s)) % P
  digit = 1
  for i in range(N):
    j = N - i
    dp[j] = (dp[j] * digit) % P
    digit = (digit * 10) % P
  
  d = {}
  ans = 0
  for r in dp:
    if r in d:
      ans += d[r]
      d[r] += 1
    else:
      d[r] = 1
  print(ans)