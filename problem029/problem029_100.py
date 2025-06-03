# coding: utf-8
# 63
import math

a,b,c,d= map(float,input().split())
A = (a-c)**2+(b-d)**2
if A<0:
    A = math.fabs(A)
print(math.sqrt(A))

