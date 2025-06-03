a,b,c,k=map(int,input().split())
kk=k-a-b
if kk <= 0:
  print(min(a,k))
else:
  print(a-kk)
