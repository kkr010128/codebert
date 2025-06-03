h,w = map(int, input().split())
sl = []
for _ in range(h):
    row = list(input())
    sl.append(row)


dp = [ [10000]*w for _ in range(h) ]
dp[0][0] = 0

for h_i in range(h):
    for w_i in range(w):
        if h_i+1 < h:
            if sl[h_i][w_i] == '.' and sl[h_i+1][w_i] == '#':
                dp[h_i+1][w_i] = min( dp[h_i+1][w_i], dp[h_i][w_i]+1 )
            else:
                dp[h_i+1][w_i] = min( dp[h_i+1][w_i], dp[h_i][w_i] )

        if w_i+1 < w:
            if sl[h_i][w_i] == '.' and sl[h_i][w_i+1] == '#':
                dp[h_i][w_i+1] = min( dp[h_i][w_i+1], dp[h_i][w_i]+1 )
            else:
                dp[h_i][w_i+1] = min( dp[h_i][w_i+1], dp[h_i][w_i] )


ans = dp[h-1][w-1]
if sl[0][0] == '#': ans += 1
print(ans)
