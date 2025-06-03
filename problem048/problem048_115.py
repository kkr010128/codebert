# -*- coding:utf-8 -*-
a = int(input())
b_int = map(int, input().split())
max = -1000000
min = 1000000
total =0
for i in b_int:
    if i > max:
        max = i
    if i < min:
        min = i
    total += i
print(min, max, total)