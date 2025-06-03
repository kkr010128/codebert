h,w = map(int, input().split())
L = [input() for i in range(h)]
dp = [[10**9]*w for i in range(h)]
if L[0][0] == ".":
    dp[0][0] = 0
else:
    dp[0][0] = 1

li = ((1,0),(0,1))
for i in range(h):
    for j in range(w):
        for dy,dx in li:
            ny,nx = i+dy,j+dx
            if ny >= h or nx >= w:
                continue
            plus = 0
            if L[i][j] == "." and L[ny][nx] == "#":
                plus =1
            dp[ny][nx] = min(dp[i][j]+plus,dp[ny][nx])
            
print(dp[h-1][w-1])
