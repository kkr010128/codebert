# coding: utf-8
# Your code here!
import math

num = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

result = 0
for i in range(num):
    result += abs(y[i]-x[i])
print(result)

result = 0
for i in range(num):
    result += abs(y[i] - x[i]) ** 2
result = math.sqrt(result)
print(result)

result = 0
for i in range(num):
    result += abs(y[i] - x[i]) ** 3
result = math.pow(result,1.0/3.0)
print(result)

result = 0
for i in range(num):
    if i == 0:
        result = abs(y[i] - x[i])
    else:
        if abs(y[i] - x[i]) > result:
            result = abs(y[i] - x[i])
print(result)

