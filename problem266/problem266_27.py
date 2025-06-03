x = int(input())
price = [100, 101, 102, 103, 104, 105]
 
dp = [False for _ in range(x + 1)]
 
dp[0] = True

for i in range(1, x + 1):
    for j in range(6):
        if i - price[j] >= 0:
            if dp[i - price[j]]:
                dp[i] = True
                break
    else:
        dp[i] = False
 
if dp[x]:
    print(1)
else:
    print(0)