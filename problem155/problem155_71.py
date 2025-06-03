N,M=map(int, input().split())
peaks=list(map(int, input().split()))
flag=[1]*N
a=0
b=0
for i in range(M):
  a,b=map(int,input().split())
  a-=1
  b-=1
  if peaks[a]<=peaks[b]:
     flag[a]=0
  if peaks[a]>=peaks[b]:
     flag[b]=0
ans=0
for i in flag:
  ans+=i
print(ans)