import math
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
d=0
for i in range(n):
  d += max(x[i],y[i])-min(x[i],y[i])
print(float(d))

d=0
for i in range(n):
  d+=(x[i]-y[i])**2
print(math.sqrt(d))

d=0
for i in range(n):
  d+=(max(x[i],y[i])-min(x[i],y[i]))**3
print(math.pow(d,1/3))

d=[]
for i in range(n):
  d.append(max(x[i],y[i])-min(x[i],y[i]))
print(float(max(d)))
