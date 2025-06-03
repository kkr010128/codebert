X,Y = map(int,input().split())

check = False
for i in range(0,X+1):
  for j in range(0,X+1):
    if i + j == X and 2*i + 4*j == Y:
      check = True
      
if check:
  print("Yes")
else:
  print("No")