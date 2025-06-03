n = int(input())

dp = [0]*(n+1)

for i in range(1,n+1):
  x = n//i
  for j in range(1,x+1):
    dp[i*j]+=1
    
sum_div = 0
for i in range(1,n+1):
  sum_div += i*dp[i]
print(sum_div)