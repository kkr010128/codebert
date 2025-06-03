X,Y = map(int,input().split())

for i in range(2*X):
  for j in range(2*X):
    if i+j == X and 2*i+4*j == Y:
      print("Yes")
      exit()
else:
  print("No")