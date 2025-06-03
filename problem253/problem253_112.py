n,a,b=map(int,input().split())
if a%2==b%2:
  c=(b-a)//2
  if (c+1)*2<=b-a:
    c+=1
  print(c)
else:
  t=min(b-1+a,n-a+n-b+1)
  c=t//2
  if (c+1)*2<=t:
    c+=1
  print(c)