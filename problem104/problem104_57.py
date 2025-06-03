a,b,c=map(int,input().split())
d=b//c
e=a//c
if a%c==0:
  print(d-e+1)
else:
  print(d-e)