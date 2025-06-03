x,k,d=map(int,input().split())
x=abs(x)
y=x//d
if k<=y:
  print(x-k*d)
else:
  if (k-y)%2==0:
    print(x-y*d)
  else:
    print(abs(d-x+y*d))