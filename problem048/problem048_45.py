# -*- coding: utf-8 -*-

n = input()
a = map(int, raw_input().split())

max = a[0]
min = a[0]
sum = 0

for i in range(n):
    if a[i] > max:
        max = a[i]
    elif a[i] < min:
        min = a[i]
    else:
        pass
    sum += a[i]

print "%d %d %d" %(min, max, sum)