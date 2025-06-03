h,w,k = map(int, input().split())
item = [[0 for _ in range(w)] for _ in range(h)]
for i in range(k):
    y,x,v = list(map(int,input().split()))
    item[y-1][x-1]=v

dp = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(4)]

for y in range(h):
    for x in range(w):
        for i in range(4):
            if y<h-1:
                dp[0][y+1][x]=max(dp[0][y+1][x],dp[i][y][x])
            if x<w-1:
                dp[i][y][x+1]=max(dp[i][y][x+1],dp[i][y][x])

        if item[y][x]>0:
            for i in range(3):
                if y<h-1:
                    dp[0][y+1][x]=max(dp[0][y+1][x],dp[i][y][x] + item[y][x])
                if x<w-1:
                    dp[i+1][y][x+1]=max(dp[i+1][y][x+1],dp[i][y][x] + item[y][x])

ans=[dp[0][-1][-1] + item[-1][-1],
     dp[1][-1][-1] + item[-1][-1],
     dp[2][-1][-1] + item[-1][-1],
     dp[3][-1][-1]]
print(max(ans))