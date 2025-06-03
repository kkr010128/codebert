X,K,D=(int(x) for x in input().split())
x=abs(X)
a=x//D
 
b=x-a*D
B=abs(x-(a+1)*D)
 
if b>B:
  a=a+1
 
if a>=K:
  print(abs(x-K*D))
 
else:
  c=K-a
  if c%2 == 0:
    print(abs(x-a*D))
  else:
    d=abs(x-(a-1)*D)
    e=abs(x-(a+1)*D)
    print(min(d,e))