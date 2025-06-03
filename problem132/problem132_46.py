N, K = map(int, input().split())
A = list(map(int, input().split()))

isMax = False
while K > 0 and not isMax:
    isMax = True
    B = [0] * N
    for i, d in enumerate(A):
        l = max(0, i - d)
        B[l] += 1
        r = i + d + 1
        if r < N:
            B[r] -= 1
    for i in range(N - 1):
        isMax &= (B[i] >= N)
        B[i + 1] += B[i]
    A = B
    K -= 1

print(*A[:N])
