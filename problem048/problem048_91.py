# -*- coding:utf-8 -*-

n = int(input())
data = input()
data = data.split()

for i in range(len(data)):
    data[i] = int(data[i])

sum = 0
for i in range(n):
    sum += data[i]
print(min(data), max(data), sum, sep = ' ')