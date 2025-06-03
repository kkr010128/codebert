N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
L = [-1] * (N+1)
L[1] = 0
idx = 1
for i in range(1, N+1):
    idx = A[idx]
    if L[idx] >= 0:
        t = i - L[idx]
        b = L[idx]
        break
    else:
        L[idx] = i

if K <= b:
    print(L.index(K))
else:
    print(L.index((K-b)%t+b))
