N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

MAX_A = 1000001

dp = [0]*MAX_A

for i in A:
  if dp[i] == 0:
    for j in range(i, MAX_A,i):
      dp[j] += 1
  else:
    dp[i] += 1

c = 0
for i in A:
  if dp[i] == 1:
    c += 1

print(c)