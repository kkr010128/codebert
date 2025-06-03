N,K = map(int,input().split())
A = list(map(int,input().split()))

for _ in range(K):
    imos = [0] * (N+1)
    for i,a in enumerate(A):
        l = max(0, i-a)
        r = min(N, i+a+1)
        imos[l] += 1
        imos[r] -= 1
    for i in range(N):
        imos[i+1] += imos[i]
    imos.pop()
    A = imos
    if all(a==N for a in A): break
print(*A)