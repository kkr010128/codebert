# coding:utf-8
import math

a,b,C=list(map(float,input().split()))

h=b*math.sin(math.radians(C))
S=a*h/2

c=math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C)))
L=a+b+c

print('%.6f'%S)
print('%.6f'%L)
print('%.6f'%h)