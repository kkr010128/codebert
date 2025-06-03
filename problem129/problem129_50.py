N=int(input())
A=sorted(list(map(int,input().split())))
m=A[-1]
dp=[True]*m
ans,p,q=0,0,False
for a in A:
  if p==a and q:
    ans-=1
    q=False
  if dp[a-1]:
    p,q=a,True
    ans+=1
    aa=a
    while m>=aa:
      dp[aa-1]=False
      aa+=a
print(ans)