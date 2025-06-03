H, N = map(int,input().split())
X = [list(map(int, input().split())) for i in range(N)]
X = sorted(X, key = lambda x:x[0])
DP = [float("inf")]*(H+X[-1][0]+X[-1][0])
DP[X[-1][0]-1] = 0
for i in range(X[-1][0], H+2*X[-1][0]):
    min = float("inf")
    for j in range(N):
        if min > DP[i-X[j][0]]+X[j][1]:
            min = DP[i-X[j][0]]+X[j][1]
        DP[i] = min

kouho = DP[H+X[-1][0]-1]
for i in range(X[-1][0]):
    if kouho > DP[H+X[-1][0]+i]:
        kouho = DP[H+X[-1][0]+i]
print(kouho)
