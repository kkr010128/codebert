def f(x):
    cnt=0
    for i in range(N):
        num=x//F[i]
        if A[i]>num:
            cnt+=A[i]-num
    return cnt

N,K=map(int,input().split())
A=list(map(int,input().split()))
F=list(map(int,input().split()))

A.sort()
F.sort(reverse=True)

low=0
high=10**12+1
while high-low>0:
    mid=(high+low)//2
    xxx=f(mid)
    if xxx<=K:
        high=mid
    else:
        if low==mid:
            low=high
        else:
            low=mid

print(low)