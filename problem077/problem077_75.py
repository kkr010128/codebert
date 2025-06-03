a,b,c,d=map(int,input().split())
ans=-10**20
if ans<a*c:
  ans=a*c
if ans<a*d:
  ans=a*d
if ans<b*c:
  ans=b*c
if ans<b*d:
  ans=b*d
print(ans)
