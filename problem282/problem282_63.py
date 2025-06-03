N,T = map(int,input().split())
data = [0] * N

M = 0
for i in range(N):
    data[i] = list(map(int,input().split()))
    M = max(M,data[i][0])

dp1 = [[0]*T for i in range(N)]

for j in range(T):
    if j < data[0][0]:
        dp1[0][j] = 0
    else:
        dp1[0][j] = data[0][1]

for j in range(T):
    for i in range(1,N):
        if data[i][0] <= j:
            dp1[i][j] = max(dp1[i-1][j],dp1[i-1][j-data[i][0]]+data[i][1])
        else:
            dp1[i][j] = dp1[i-1][j]

dp2 = [[0]*T for i in range(N)]

for j in range(T):
    if j < data[N-1][0]:
        dp2[N-i][j] = 0
    else:
        dp2[N-1][j] = data[N-1][1]

for j in range(T):
    for i in range(N-2,-1,-1):
        if data[i][0] <= j:
            dp2[i][j] = max(dp2[i+1][j],dp2[i+1][j-data[i][0]]+data[i][1])
        else:
            dp2[i][j] = dp2[i+1][j]

m = 0

for j in range(T):
    for i in range(N):
        if i == 0:
            m = max(m,dp2[i+1][T-1-j] + data[i][1])
        elif i == N-1:
            m = max(m,dp1[i-1][j] + data[i][1])
        else:
            m = max(m,dp1[i-1][j] + dp2[i+1][T-1-j] + data[i][1])

print(m)