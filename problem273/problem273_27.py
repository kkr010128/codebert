from collections import defaultdict
N,K=map(int, input().split())
A=list(map(int,input().split()))
"""count=0
for l in range(N):
    if A[l]%K==1:
        count+=1
for l in range(N-1):
    sum=A[l]
    for r in range(l+1,N):
        sum+=A[r]
        if sum%K==r-l+1:
            count+=1
print(count)"""
cum=[0]*(N+1)
for i in range(N):
    cum[i+1]=(cum[i]+A[i]-1)%K
dic=defaultdict(int)
ans=0
for i in range(N+1):
    ans+=dic[cum[i]]
    dic[cum[i]]+=1
    if i-(K-1)>=0:
        dic[cum[i-(K-1)]]-=1
print(ans)
