import math
mod = 10**9+7

N = int(input())
M = math.ceil(N/3)+1
x = [[0]*(N+1) for _ in range(M)]

for i in range(3,N+1):
    x[1][i] = 1

for i in range(2,M):
    for j in range(i*3,N+1):
        x[i][j] = (x[i][j-1] + x[i-1][j-3]) % mod
ans = 0
for i in range(1,M):
    ans = (ans + x[i][N]) % mod
print(ans)