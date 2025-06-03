N, M, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Asum = [0]
Bsum = [0]
a = 0
b = 0
for i in range(N):
    a += A[i]
    Asum.append(a)
for i in range(M):
    b += B[i]
    Bsum.append(b)
Asum.append(0)
Bsum.append(0)
res, j = 0, M
for i in range(N+1):
    if Asum[i] > K:
        break
    while Asum[i] + Bsum[j] > K:
        j -= 1
    res = max(res,i+j)
print(res)