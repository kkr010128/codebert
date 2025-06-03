
X = int(input())
flag = 0
for i in range(-150,150):
  for j in range(-150,150):
    if(i**5 - j**5 == X):
      print(i,j)
      flag = 1
      break
  if(flag==1):
    break