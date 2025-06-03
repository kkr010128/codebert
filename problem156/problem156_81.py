x = int(input())
n = 120
for i in range(n):
  for j in range(i):
    if x == i**5-j**5:
      print(i,j)
      exit(0)
    if x == i**5+j**5:
      print(i,-j)
      exit(0)