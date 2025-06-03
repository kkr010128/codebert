N,T = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(N)]
AB.sort(key=lambda x: x[0])
#print(AB)

W = T + 1
def dp(AB,W):
    N = len(AB)
    DP = [[0]*W for i in range(N+1)]
    for i in range(N):
        for w in range(W):
            if w != W-1:
                if AB[i][0] <= w:
                    DP[i+1][w] = max(DP[i][w-AB[i][0]]+AB[i][1],DP[i][w])
                else:
                    DP[i+1][w] = DP[i][w]
            else:
                DP[i+1][w] = max(DP[i][w-1]+AB[i][1],DP[i][w])
    return DP

DP1 = dp(AB,W)

ans = DP1[N][T]
print(ans)