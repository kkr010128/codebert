a,b = map(int,input().split())
if a >= 10:
  print(str(b))
else:
  print(str(b+100*(10-a)))