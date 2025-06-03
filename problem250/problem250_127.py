X = int(input())

while True:
  flag = True
  for i in range(2,X):
    if X%i == 0:
      flag = False
      break
  if flag:
    break
  X += 1
  
print(X)