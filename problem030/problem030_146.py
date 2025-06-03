#coding:utf-8
#1_10_B 2015.4.14

import math

a,b,C = map(int,input().split())
C = math.radians(C)
h = b * math.sin(C)
S = a * h / 2
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))
print('{:.10f}\n{:.10f}\n{:.10f}'.format(S,L,h))