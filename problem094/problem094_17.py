from itertools import accumulate
R, C, K = map(int, input().split())
vss = [[None]*C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    vss[r-1][c-1] = v

dp = []

for y in range(R):
    ndp = []
    for x in range(C):
        tmp = []
        uemax = 0
        if y > 0:
            uemax = max(dp[x])
        if vss[y][x] is None:
            if x > 0:
                left = ndp[-1]
                tmp.append(left[0] if left[0] > uemax else uemax)
                tmp.append(left[1])
                tmp.append(left[2])
                tmp.append(left[3])
            else:
                tmp.append(uemax)
                tmp.append(0)
                tmp.append(0)
                tmp.append(0)
        else:
            v = vss[y][x]
            if x > 0:
                left = ndp[-1]
                tmp.append(left[0] if left[0] > uemax else uemax)
                tmp.append(max(left[0]+v, left[1], uemax+v))
                tmp.append(left[1]+v if left[1]+v > left[2] else left[2])
                tmp.append(left[2]+v if left[2]+v > left[3] else left[3])
            else:
                tmp.append(uemax)
                tmp.append(uemax + v)
                tmp.append(0)
                tmp.append(0)
        ndp.append(tmp)
    dp = ndp

print(max(dp[-1]))
