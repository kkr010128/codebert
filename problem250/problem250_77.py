import math
x = int(input())
ans =x

for j in range(x,2*x):
  flag=1
  for i in range(2,int(math.sqrt(x))+1):
    if x%i==0:
      flag=0
  if flag==1:
    print(x)
    exit(0)
  x+=1