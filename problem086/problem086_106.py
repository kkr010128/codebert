n,x,t=map(int,input().split())
a=n%x
b=int(n/x)
if a==0:
  c=b
else:
  c=b+1
d=c*t
print(d)