ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))
n = ii()

def get_head(x):
    while x:
        b = x%10
        x //= 10
    return b

dp = [[0] * 10 for i in range(10)]
for i in range(1,n+1):
    h = get_head(i)
    t = i%10
    dp[h][t] += 1

for i in range(10):
    dp[0][i] = 0
    dp[i][0] = 0

ans = 0
for i in range(1,n+1):
    h = get_head(i)
    t = i%10
    ans += dp[t][h]

print(ans)
