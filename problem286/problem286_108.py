a,b=map(int,input().split())
if (a>=10) or (b>=10):
  print(-1)
  exit()
else:
  print(a*b)