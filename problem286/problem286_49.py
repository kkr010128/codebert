x = list(map(int,input().split()))

if(len(str(x[0])) < 2 and len(str(x[1])) < 2):
  print(x[0] * x[1])
else:
  print(-1)