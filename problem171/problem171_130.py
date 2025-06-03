n = int(input())

ai = [int(i) for i in input().split()]

ai_li = []

for i in range(n):
    ai_li.append([ai[i],i+1])

ai_li.sort(reverse=True)

dp = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(1,n+1):
    #print(i)
    for j in range(0,i+1):
        if i == 1:
            if j == 1:
                dp[i][j] = ai_li[i-1][0]*abs(ai_li[i-1][1]-1)
            else:
                dp[i][j] = ai_li[i-1][0]*abs(n-ai_li[i-1][1])
        else:
            if j == 0:
                #print(dp[i][j])
                dp[i][j] = dp[i-1][0] + ai_li[i-1][0]*abs(n-ai_li[i-1][1]-i+1)
            else:
                #if i == 2:
                #    print(i-1,j-1)
                dp[i][j] = max(dp[i-1][j-1]+ai_li[i-1][0]*abs(ai_li[i-1][1]-j),dp[i-1][j]+ai_li[i-1][0]*abs(n-ai_li[i-1][1]-(i-1-j)))
                #dp[i][j] = max(dp[i-1][j-1]+ai_li[i][0]*abs(ai_li[i][1]-1+i-1),dp[i-1][j]+ai_li[i][0]*abs(n-i+1-ai_li[i][1]))

#print(dp)
print(max(dp[n]))