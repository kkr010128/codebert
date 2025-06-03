N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

T = []
for i in range(N):
    T.append(A[i]*F[i])

s = -1
l = 10**12
while(l-s > 1):
    mid = (l-s)//2 + s
    c = 0
    for i in range(N):
        if T[i] > mid:
            if (T[i] - mid) % F[i] == 0:
                c += (T[i] - mid) // F[i]
            else:
                c += (T[i] - mid) // F[i] + 1
    if c > K:
        s = mid
    else:
        l = mid
print(l)