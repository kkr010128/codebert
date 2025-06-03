N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
for _ in range(K):
    B = [0]*(N+1)
    for i in range(N):
        l = max(0, i-A[i])
        r = min(N-1, i+A[i])
        B[l] += 1
        B[r+1] -= 1
    for i in range(N):
        B[i+1] += B[i]
    A = B[:N]
    if all([x == N for x in A]):
        break
print(*A)