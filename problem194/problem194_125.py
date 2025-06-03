h,w = map(int,input().split())
s = [list(str(input())) for i in range(h)]
dp = [[10 ** 10] * w for i in range(h)]
if s[0][0] == "#":dp[0][0] = 1
else:dp[0][0] = 0
for i in range(w):
    for j in range(h):
        if s[j][i] == "#":
            s[j][i] = 1
        else:
            s[j][i] = 0
for i in range(1,h+w-1):
    for j in range(i+1):
        if 0 < j < h and 0 <= i-j < w:
            dp[j][i-j] = min(dp[j-1][i-j]+(s[j][i-j]&~s[j-1][i-j]),dp[j][i-j])
        if 0 < i-j < w and 0 <= j < h:
            dp[j][i-j] = min(dp[j][i-j-1]+(s[j][i-j]&~s[j][i-j-1]),dp[j][i-j])
print(dp[h-1][w-1])