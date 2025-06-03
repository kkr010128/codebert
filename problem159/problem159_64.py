from math import *
x = int(input())
a = 100
b = 0
while a < x:
 a += a//100
 b+=1
print(b)
