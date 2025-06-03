n,a,b=input().split()
n=int(n)
a=int(a)
b=int(b)
c=a+b
if n%c>a:
  print((n//c)*a+a)
else:
  print((n//c)*a+n%c)