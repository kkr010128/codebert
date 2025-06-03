N, K = map(int, input().split())
*A, = map(int, input().split())
for i in range(N-K):
    print("Yes" if A[i]<A[i+K] else "No")