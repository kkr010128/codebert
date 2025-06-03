dp = [0 for i in range(1000000)]
N = int(input())
for i in range(2,1000):
  if i**2>N:
    break
  if dp[i]!=0:
    continue
  for j in range(i,1000000,i):
    dp[j] = 1
while dp[N]!=0:
  N += 1
print(N)