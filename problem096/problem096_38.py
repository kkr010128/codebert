n,d=map(int,input().split())
e=d**2
ans=0
for m in range(n):
  a,b=map(int,input().split())
  c=a**2+b**2
  if c<=e:
    ans=ans+1
print(ans)