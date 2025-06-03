n,a,b=map(int,input().split())

p=a+b
c=n%p
d=n//p

if c<a:
  print(d*a+c)
else:
  print((d+1)*a)