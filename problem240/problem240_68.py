n,m=map(int,input().split())
a=[0]*n
ans=0
for i in range(m):
  p,s=input().split()
  p=int(p)-1
  if a[p]!=1:
    if s=='WA':a[p]-=1
    else:
      ans-=a[p]
      a[p]=1
for i in range(n):
  a[i]=max(a[i],0)
print(sum(a),ans)