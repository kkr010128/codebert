import math
X=list()
Y=list()
s=0
N=int(input())
for i in range(N):
  x,y=map(int,input().split())
  X.append(x)
  Y.append(y)
for i in range(N):
  for j in range(N):
    s+=math.sqrt(((X[i]-X[j])**2)+((Y[i]-Y[j])**2))
print(s*(1/N))