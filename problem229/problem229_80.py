h,n=map(int,input().split())
ans=0
magic=[]
al=[]
bl=[]
for i in range(n):
  a,b=map(int,input().split())
  magic.append([a,b])
  al.append(a)
  bl.append(b)
amx=max(al)
bmn=min(bl)
dp=[-1]*(h+amx+1)
dp[0]=0
for i in range(1,h+amx+1):
  mn=float("inf")
  for j in magic:
    mp=j[1]
    at=j[0]
    if at>i:
      cst=mp
    else:
      cst=dp[i-at]+mp
    if cst<mn:
      mn=cst
  dp[i]=mn
  
print(min(dp[h:]))
