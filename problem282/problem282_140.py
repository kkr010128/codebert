N,T = list(map(int,input().split()))

A =[list(map(int,input().split())) for i in range(N)]

A.sort(key = lambda x:x[0])

INF = float("inf")

DP = [[-INF]*(T+3001) for i in range(N+1)]

DP[0][0] = 0

for i in range(N):
    for j in range(T):
        DP[i+1][j] = max(DP[i+1][j],DP[i][j])
        DP[i+1][j+A[i][0]] = max(DP[i+1][j+A[i][0]],DP[i][j+A[i][0]],DP[i][j]+A[i][1])
score = 0
for i in range(N):
    for j in range(T+A[i][0]):
        score = DP[i+1][j] if DP[i+1][j]>score else score

print(score)