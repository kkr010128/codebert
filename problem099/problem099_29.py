N,K = map(int,input().split())
A = list(map(int,input().split()))
if K==0:
    high = max(A)
else:
    low = 0
    high = 10**9
    while high-low>1:
        mid = (high+low)//2
        cnt = 0
        for i in range(N):
            if A[i]%mid==0:
                cnt += A[i]//mid-1
            else:
                cnt += A[i]//mid
        if K>=cnt:
            high = mid
        else:
            low = mid
print(high)