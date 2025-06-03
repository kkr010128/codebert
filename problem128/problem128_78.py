x,n = map(int, input().split())
if n!=0:
  p = list(map(int,input().split()))
  for i in range(0,101):
    if x-i not in p:
      print(x-i)
      break
    elif x+i not in p:
      print(x+i)
      break
else:
  print(x)