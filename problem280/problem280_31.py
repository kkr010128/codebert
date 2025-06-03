import math
N = int(input())
x = []
y = []
for i in range(N):
  tmp = input().split(" ")
  x.append(int(tmp[0]))
  y.append(int(tmp[1]))

d = 0
for i in range(N):
  for j in range(N):
    d += math.sqrt((x[j]-x[i]) ** 2 + (y[j]-y[i]) ** 2)

print(d/N)