n,a,b=map(int,input().split())
if (b-a)%2==0:
  print((b-a)//2)
else:
  c=min(b-1,n-a)
  e=min(a-1,n-b)
  d=(b-a-1)//2+e+1
  print(min(c,d))