
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

x = [0] * (N + 1)
y = [0] * (M + 1)
for i in range(N):
    x[i + 1] = x[i] + A[i]

for i in range(M):
    y[i + 1] = y[i] + B[i]

j = M
ans = 0
for i in range(N + 1):
    if x[i] > K:
        continue
    while j >= 0 and x[i] + y[j] > K:
        j -= 1
    ans = max(ans, i + j)
print(ans)
