X=int(input())
n=X%100
m=X//100
if 0<=n<=m*5:
  print(1)
else:
  print(0)
