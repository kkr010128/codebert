dp = [True]  # i円の買い物ができるか
x = int(input())
for i in range(99):
    dp.append(False)
for i in range(100, x + 1):
    if(i < 106):
        dp.append(True)
    else:
        if(dp[i - 100] or dp[i - 101] or dp[i - 102] or dp[i - 103] or dp[i - 104] or dp[i - 105]):
            dp.append(True)
        else:
            dp.append(False)
if(dp[x]):
    print(1)
else:
    print(0)
