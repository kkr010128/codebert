#coding:utf-8
#1_10_B 2015.4.14
import math

a,b,C = list(map(int,input().split()))
rad = math.pi * C / 180
S = a * b * math.sin(rad) / 2
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad))
L = a + b + c
h = S * 2 / a
print('{:.10f}\n{:.10f}\n{:.10f}'.format(S,L,h))