import math
n,d=map(int,input().split())
L=[list(map(int, input().split())) for i in range(n)]
x=0
for i in range(n):
  if math.sqrt(L[i][0]**2+L[i][1]**2)<=d:
    x+=1
  else:
    pass
print(x)