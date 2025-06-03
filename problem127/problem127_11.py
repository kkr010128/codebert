import sys
x,y = map(int,input().split())
for i in range(x+1):
  for j in range(x-i+1):
    if i+j == x and (i*2)+(j*4) == y:
      print("Yes")
      sys.exit()
print("No")