N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
for k in range(K):
    B = [0] * (N+1)
    for i, a in enumerate(A):
        l = max(0, i-a)
        r = min(i+a+1, N)
        B[l] += 1
        B[r] -= 1
    for i in range(1, N+1):
        B[i] += B[i-1]
    B.pop()
    if (A==B): break
    A = B
for a in A:
    print(a, end=' ')
print()
