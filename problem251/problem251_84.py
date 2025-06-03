n,k = map(int,input().split())
R,S,P = map(int,input().split())
T = input()
slist = ['']*k
for i in range(n):
    slist[i%k] += T[i]

ans = 0
for s in slist:
    dp = [[0,0,0]for i in range(len(s))]
    #dp[i][j] = 直前にｊを出したときの得点の最大値
    '''
    0..r
    1..s
    2..p
    '''
    dp[0][1] = S if s[0] == 'p' else 0
    dp[0][0] = R if s[0] == 's' else 0
    dp[0][2] = P if s[0] == 'r' else 0

    for i in range(1,len(s)):
        if s[i] == 'r':
            dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + P
            dp[i][1] = max(dp[i-1][0],dp[i-1][2])
            dp[i][0] = max(dp[i-1][1],dp[i-1][2])
        elif s[i] == 's':
            dp[i][0] = max(dp[i-1][2],dp[i-1][1]) + R
            dp[i][1] = max(dp[i-1][0],dp[i-1][2])
            dp[i][2] = max(dp[i-1][1],dp[i-1][0])
        else:
            dp[i][1] = max(dp[i-1][2],dp[i-1][0]) + S
            dp[i][0] = max(dp[i-1][1],dp[i-1][2])
            dp[i][2] = max(dp[i-1][1],dp[i-1][0])
    
    ans += max(dp[len(s)-1][0],dp[len(s)-1][1],dp[len(s)-1][2])
#print(slist)
print(ans)

