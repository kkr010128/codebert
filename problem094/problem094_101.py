R, C, K = map(int, input().split())
item = {}
for _ in range(K):
    r, c, v = map(int, input().split())
    item[(r, c)] = v

dp = [[0] * 4 for _ in range(3010)]
ndp = [[0] * 4 for _ in range(3010)]
for r in range(1, R+1):
    for c in range(1, C+1):
        prer = max(dp[c])
        ndp[c][0] = max(prer, ndp[c-1][0])
        ndp[c][1] = max(prer, ndp[c-1][1])
        ndp[c][2] = max(prer, ndp[c-1][2])
        ndp[c][3] = max(prer, ndp[c-1][3])
        if item.get((r, c)):
            ndp[c][1] = max(ndp[c][1], max(prer, ndp[c-1][0]) + item[(r,c)])
            ndp[c][2] = max(ndp[c][2], max(prer, ndp[c-1][1]) + item[(r,c)])
            ndp[c][3] = max(ndp[c][3], max(prer, ndp[c-1][2]) + item[(r,c)])
    dp = ndp
    ndp = [[0] * 4 for _ in range(3010)]

#print(dp)
print(max(dp[C]))
