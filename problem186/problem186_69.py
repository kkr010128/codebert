[K, N] = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

t = K - A[N-1] + A[0]
for i in range(N-1):
    if t < A[i+1] - A[i]:
        t = A[i+1] - A[i]

print(K-t)