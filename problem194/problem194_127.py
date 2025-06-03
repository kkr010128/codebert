def main():
    h,w = map(int,input().split(" "))
    s = [list(input()) for i in range(h)]
    
    dp = [[0]*w for i in range(h)]
    dp[0][0] = 1 if s[0][0]=="#" else 0

    for i in range(1,h):
        sgmdown = 1 if s[i][0]=="#" and s[i-1][0]=="." else 0
        dp[i][0] = dp[i-1][0] + sgmdown
    
    for j in range(1,w):
        sgmright = 1 if s[0][j]=="#" and s[0][j-1]=="." else 0
        dp[0][j] = dp[0][j-1] + sgmright

    for i in range(1,h):
        for j in range(1,w):
            sgmdown = 1 if s[i][j]=="#" and s[i-1][j]=="." else 0
            sgmright = 1 if s[i][j]=="#" and s[i][j-1]=="." else 0
            dp[i][j] = min(dp[i-1][j]+sgmdown, dp[i][j-1]+sgmright)

    print(dp[h-1][w-1])
main()