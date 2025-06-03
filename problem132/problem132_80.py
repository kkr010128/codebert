N, K = map(int, input().split())
A = [int(x) for x in input().split()]
 
K = min(K, 41)
 
# imos
for _ in range(K):
    B = [0 for _ in range(N)]
    for i in range(N):
        l = max(0, i-A[i])
        r = min(N-1, i+A[i])
        B[l] += 1
        if r+1 < N:
            B[r+1] -= 1
    for i in range(1, N):
        B[i] += B[i-1]
    A = B

print(*A)