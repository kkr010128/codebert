n,k=map(int,input().split())
r,s,p=map(int,input().split())
d={'r':p,'s':r,'p':s}
t=input()
ans=0
for i in range(k):
  a=t[i::k]
  flag=a[0]
  cnt=2
  for j in a[1:]:
    if j!=flag:
      ans+=d[flag]*(cnt//2)
      flag=j
      cnt=2
    else:cnt+=1
  ans+=d[flag]*(cnt//2)
print(ans)