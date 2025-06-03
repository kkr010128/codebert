X = int(input())
Food = [100,101,102,103,104,105]
dp = [False] * (X+1)
dp[0] = True
for i in range(X+1):
    for f in Food:
        if i - f >= 0:
            #print(i,i-f)
            dp[i] = dp[i - f] | dp[i]
print('1' if dp[X] else '0')
