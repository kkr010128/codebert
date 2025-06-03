N, K=map(int, input().split())
A=list(map(int, input().split()))
F=list(map(int, input().split()))
A.sort()
F.sort(reverse=True)
l=-1
r=10**12+10
while l+1<r:
    mid=(l+r)//2
    s=0
    for i in range(N):
        s+=max(0, A[i]-mid//F[i])
    if s<=K:
        r=mid
    else:
        l=mid
print(r)
