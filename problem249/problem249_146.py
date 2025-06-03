a,b,k=map(int,input().split())

s=k-a
t=k-a-b

if s>=0:
  if t>=0:
    print(0,0)
  else:
    print(0,a+b-k)
else:
  print(a-k,b)