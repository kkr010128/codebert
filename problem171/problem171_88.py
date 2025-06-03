from collections import deque

N = int(input())
A = sorted([(int(j),i) for i, j in enumerate(input().split())])[::-1]
d = deque([(0,0)])
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
while(len(d)>0):
    i, j = d.pop()
    if i + j > N - 1:
        continue
    tmp = dp[i][j] + A[i+j][0] * abs(A[i+j][1] - i)
    if tmp > dp[i+1][j]:
        if dp[i+1][j] == 0:
            d.appendleft((i+1,j))
        dp[i+1][j] = tmp
    tmp = dp[i][j] + A[i+j][0] * abs(A[i+j][1] - N + j + 1)
    if tmp > dp[i][j+1]:
        if dp[i][j+1] == 0:
            d.appendleft((i,j+1))
        dp[i][j+1] = tmp
        
ans = -1
for i in range(N):
    for j in range(N):
        if dp[i][j] > ans:
            ans = dp[i][j]
print(ans)