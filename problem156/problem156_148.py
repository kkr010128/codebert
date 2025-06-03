n=int(input())
a=False
for i in range(200):
  for j in range(200):
    if i**5-j**5==n:
      print(i,j)
      a=True
    elif i**5+j**5==n:
      print(i,-j)
      a=True
  if a:
      break