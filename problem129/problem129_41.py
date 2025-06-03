n = int(input())
a = list(map(int, input().split()))
ma = max(a)
dp = [0]*(ma+1)

for i in sorted(a):
  if 1 <= dp[i]:
    dp[i] += 1
    continue

  for j in range(1, ma//i + 1):
    dp[j * i] += 1

ans=0
for i in a:
  if dp[i] == 1:
    ans += 1
print(ans)