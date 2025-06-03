import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)

bh = 10**12
bl = 0
m = 10**6
while True:
    t = K
    for i in range(len(A)):
        if A[i]*F[i] > m:
            t -= A[i] - int(m / F[i])
            if t < 0:
                break
    if t >= 0:
        bh = m
        m = (bh + bl) // 2
    else:
        bl = m + 1
        m = (bh + bl) // 2
    if bh == bl:
        print(bh)
        exit(0)
