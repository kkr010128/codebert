x = int(input())

dp = [0]*200000
for j in range(6):
  dp[100+j] += 1

def max_sum():
  global dp
  for i in range(x):
    if dp[i] > 0:
      for j in range(6):
        dp[i+100+j] += 1
  return


max_sum()
print(min(dp[x], 1))