import math
n = int(input())
x = list(map(float, (input().split())))
y = list(map(float, (input().split())))
l = [0.0]*n

for i in range(n):
    l[i] = abs(x[i]-y[i])
print(sum(l))
che = max(l)

for i in range(n):
    l[i] = abs(x[i]-y[i])**2
print(math.sqrt(sum(l)))

for i in range(n):
    l[i] = abs(x[i]-y[i])**3
print(math.pow(sum(l), 1.0/3.0))
print(che)