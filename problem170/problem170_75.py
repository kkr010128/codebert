N, K = map(int, input().split())
A = [0]*(N+2)
for i in range(N+1):
    A[i+1] += A[i] + i
ans = 0
for i in range(K, N+2):
    minv = A[i]
    maxv = A[N+1]-A[N-i+1]
    ans += maxv-minv+1
    ans %= 10**9+7
print(ans)
