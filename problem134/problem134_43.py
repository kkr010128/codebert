n=int(input())
L=list(map(int,input().split()))
if L.count(0)!=0:
  print(0)
else:
  L_1=sorted(L)
  x=1
  for i in range(n):
    x*=L_1[i]
    if x>10**18:
      x=-1
      break
  print(x)