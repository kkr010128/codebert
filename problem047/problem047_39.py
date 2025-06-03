# -*- coding:utf-8 -*-
import sys
array = []
for i in sys.stdin:
    array.append(i)

for i in range(len(array)):
    data = array[i].split()
    a = int(data[0])
    op = str(data[1])
    b = int(data[2])
    if op == '?':
        break
    if op == '+':
        print(a+b)
    if op == '-':
        print(a-b)
    if op == '/':
        print(int(a/b))
    if op == '*':
        print(a*b)