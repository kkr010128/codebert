N, K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))
A.sort(reverse=True)
F.sort()
U = 10**12
L = -1
while U - L > 1:
    x = (U+L)//2
    cnt = 0
    for i in range(N):
        if x//F[i] < A[i]:
            cnt += A[i] - x//F[i]
    if cnt > K:
        L = x
    else:
        U = x
print(U)