a,b=map(int,input().split())
if a<0 or a>9:
  print(-1)
elif b<0 or b>9:
  print(-1)
else:
  print(a*b)