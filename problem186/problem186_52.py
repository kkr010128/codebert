K, N = map(int, input().split())
A = tuple(map(int, input().split()))

maxd = K - A[-1] + A[0]
for i in range(1, N):
    d = A[i] - A[i-1]
    maxd = max(maxd, d)
ans = K - maxd
print(ans)