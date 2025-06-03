#70 C - 100 to 105 WA
X = int(input())

dp = [0]*(100010)
lst = [100,101,102,103,104,105]
for i in range(100,106):
    dp[i] = 1

# dp[v] が存在するなら 1, しないなら 0
for v in range(100,X+1):
    for w in range(6):
        n = lst[w]
        if dp[v-n] == 1:
            dp[v] = 1
print(dp[X])