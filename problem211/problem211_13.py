a,b=map(int,input().split())
c=0
res = 0
if a >=10:
  print(b)
else:
  c = 100 * (10-a)
  res = b+c
  print(res)