#coding: utf-8
import math

n = int(input())
x = [int(i) for i in input().split(" ")]
y = [int(i) for i in input().split(" ")]

d1 = d2 = d3 = di = 0
for i in range(n):
    d1 += abs(x[i] - y[i])
    d2 += abs(x[i] - y[i])**2
    d3 += abs(x[i] - y[i])**3
    if di < abs(x[i] - y[i]):
        di = abs(x[i] - y[i])

print(d1)
print(math.pow(d2, 1.0/2.0))
print(math.pow(d3, 1.0/3.0))
print(di)
