N = int(input())
A = [int(x) for x in input().split()]
M = max(A)

count = [0 for _ in range(M + 1)]
for i in range(N):
    count[A[i]] += 1

S = 0
for i in range(M + 1):
    m = count[i]
    S += (m * (m - 1)) // 2

ans = [S for _ in range(N)]
for i in range(N):
    m = count[A[i]]
    ans[i] -= m - 1

for i in range(N):
    print(ans[i])