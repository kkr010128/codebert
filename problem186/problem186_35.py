K, N = map(int, input().split())
A = list(map(int, input().split()))
ans = K
for i in range(N):
    start = A[i]
    end = K+A[i-1] if A[i-1] < A[i] else A[i-1]
    path = end-start
    ans = min(path, ans)

print(ans)