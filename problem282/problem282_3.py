n,t = map(int,input().split())
L = []
for i in range(n):
    a,b = map(int,input().split())
    L.append([a,b])
dp1 = [[0 for i in range(t)] for i in range(n+1)]
dp2 = [[0 for i in range(t)] for i in range(n+1)]
for i in range(n):
    a = L[i][0]
    b = L[i][1]
    for j in range(t):
        if j-a >= 0:
            dp1[i+1][j] = max(dp1[i][j], dp1[i][j-a]+b, dp1[i+1][j])
        else:
            dp1[i+1][j] = max(dp1[i][j],dp1[i+1][j])
for i in range(n):
    a = L[n-i-1][0]
    b = L[n-i-1][1]
    if i == 0:
        for j in range(a, t):
            dp2[n-i-1][j] = b
    else:
        for j in range(t):
            if j-a >= 0:
                dp2[n-i-1][j] = max(dp2[n-i][j], dp2[n-i][j-a]+b,dp2[n-i-1][j])
            else:
                dp2[n-i-1][j] = max(dp2[n-i-1][j], dp2[n-i][j])
ans = 0
for i in range(1,n+1):
    for j in range(t):
        ans = max(ans, dp1[i-1][j]+dp2[i][t-1-j]+L[i-1][1])
print(ans)
