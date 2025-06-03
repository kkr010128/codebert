import bisect

N=int(input())
L=list(map(int,input().split()))

L=sorted(L)

ans=0
for i in range(N-1):
    for k in range(i+1,N-1):
        a=L[i]+L[k]
        b=bisect.bisect_left(L,a)
        ans=ans+(b-k-1)

print(ans)