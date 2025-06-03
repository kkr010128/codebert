N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
F = sorted(list(map(int,input().split())),reverse=True)
if K>=sum(A):
    ans = 0
else:
    low = 0
    high = 10**12
    while high-low>1:
        mid = (high+low)//2
        B = A[:]
        cnt = 0
        for i in range(N):
            if B[i]*F[i]>mid:
                cnt += (B[i]-mid//F[i])
        if cnt<=K:
            high = mid
        else:
            low = mid
    ans = high
print(ans)