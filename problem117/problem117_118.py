import bisect
N, M, K = map(int, input().split())
A = [0]+[int(i) for i in input().split()]
B = [int(i) for i in input().split()]

for i in range(1, N+1):
    A[i] = A[i-1]+A[i]

for i in range(1, M):
    B[i] = B[i-1]+B[i]


ans = 0
for i in range(N+1):
    if A[i] <= K:
        ans = max(ans, i+bisect.bisect_right(B, K-A[i]))
print(ans)
