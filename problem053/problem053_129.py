# -*- coding:utf-8 -*-

n = int(input())
import sys
a = input()
a = a.split()
a = [int(i) for i in a]
a.reverse()

for i in range(n-1):
    print(a[i],end = ' ')
print(a[n-1])