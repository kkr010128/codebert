n,t = map(int,input().split())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
l.sort(key=lambda x:x[0])
dp = [[0 for i in range(t)] for i in range(n+1)]
al = []
for i in range(n):
    a,b = l[i]
    for j in range(t):
        if dp[i][j] == 0:
            if j == 0:
                if j + a < t:
                    dp[i+1][j+a] = max(dp[i][j+a],b)
                else:
                    al.append(b)
        else:
            if j + a < t:
                dp[i+1][j+a] = max(dp[i][j+a],dp[i][j]+b)
            else:
                al.append(dp[i][j]+b)
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
if len(al) > 0:
    print(max(max(dp[n]),max(al)))
else:
    print(max(dp[n]))