a,b=map(int,input().split())
g=1
while 1:
  if a==b:
    g=a
    break
  if a<b:
    k=a
    a=b
    b=k
  a-=b
ans=1
i=2
while i*i<=g:
  if g%i==0:
    ans+=1
    while g%i==0:
      g//=i
  i+=1
if g!=1:
  ans+=1
print(ans)