import bisect
N=int(input())

rllist=[]
for _ in range(N):
  X,L=map(int,input().split())
  rllist.append((X+L,X-L))
rllist.sort()
#print(rllist)

dp=[0]*N
dp[0]=1
for i in range(1,N):
  r,l=rllist[i]
  
  pos=bisect.bisect(rllist,(l,float("inf")))
  #print(i,pos)
  if pos==0:
    dp[i]=dp[i-1]
  else:
    dp[i]=max(dp[i-1],dp[pos-1]+1)
  
#print(dp)
print(dp[-1])