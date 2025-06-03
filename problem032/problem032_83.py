from math import *

n = input()
x = map(float, raw_input().split())
y = map(float, raw_input().split())

for i in range(1,4):
    temp = 0
    for j in range(n):
        temp += fabs(x[j]-y[j])**i
    print pow(temp,1.0/i)

d = 0
for i in range(n):
    if(fabs(x[i]-y[i]) > d):
        d = fabs(x[i]-y[i])
print d