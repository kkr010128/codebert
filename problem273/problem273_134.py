from collections import defaultdict
d=defaultdict(int)
N,K=map(int,input().split())
A=[0]+list(map(int,input().split()))
S=[None]*(N+1)
S[0]=0
cnt=0
d[0]=1
for i in range(1,N+1):
  S[i]=(S[i-1]+A[i]-1)%K
for i in range(1,N+1):
  if i-K>=0:
    d[S[i-K]]-=1
  cnt+=d[S[i]]
  d[S[i]]+=1
print(cnt)