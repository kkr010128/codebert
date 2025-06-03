from itertools import accumulate
N, K = map(int, input().split())
A = list(map(int, input().split()))
for k in range(min(50, K)):
    B = [0]*N
    for i in range(N):
        B[max(0, i-A[i])] += 1
        r = i+A[i]+1
        if r < N:
            B[r] -= 1
    A = list(accumulate(B))
print(*A)
