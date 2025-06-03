# -*- coding:utf-8 -*-

x = 100000
n = int(input())

for i in range(n):
    x = x + x*0.05
    a = x // 1000
    r = x % 1000
    if r != 0:
        x = 1000*a + 1000
    else:
        x = 1000*a
        
print(int(x))