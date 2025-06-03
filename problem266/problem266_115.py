X = int(input())
dp = [False]*(X+1)
dp[0] = True

for i in range(X+1):
    for j in range(100, 106):
        if i+j<=X:
            dp[i+j] |= dp[i]

if dp[X]:
    print(1)
else:
    print(0)