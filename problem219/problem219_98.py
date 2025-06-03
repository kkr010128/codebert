#E DPでとく
N = [int(x) for x in input()]
dp = 0,1
for item in N:
    a = min(dp[0] + item, dp[1] + 10 - item)
    b = min(dp[0] + item + 1, dp[1] + 10 - (item + 1))
    dp = a, b
    
print(dp[0])