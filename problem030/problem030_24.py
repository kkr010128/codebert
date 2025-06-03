#coding: utf-8
import math

a, b, C = (float(i) for i in input().split())
C = math.pi * C / 180
S = a * b * math.sin(C) / 2
h = b * math.sin(C)
L = a + b + math.sqrt(a**2 + b ** 2 - 2 * a * b * math.cos(C))

print("{:.8f}".format(S))
print("{:.8f}".format(L))
print("{:.8f}".format(h))

