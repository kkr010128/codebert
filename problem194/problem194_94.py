h,w = map(int,input().split())
B = [input() for _ in range(h)]
dp=[]
def ch(x1,y1,x2,y2):
    if B[x1][y1]=='.' and B[x2][y2]=='#':
        return 1
    else:
        return 0
dp = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    for j in range(w):
        if i==0 and j==0 and B[i][j]=='#':
            dp[i][j]+=1
        elif i==0:
            dp[i][j] = dp[i][j-1]+ch(i,j-1,i,j)
        elif j==0:
            dp[i][j] = dp[i-1][j]+ch(i-1,j,i,j)
        else:
            dp[i][j] = min(dp[i][j-1]+ch(i,j-1,i,j),dp[i-1][j]+ch(i-1,j,i,j))
print(dp[h-1][w-1])