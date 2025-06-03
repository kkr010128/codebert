# coding: utf-8
# Here your code !
import math
prof = 0
d = int(input())
li =[int(input()) for i in range(d)]
max=float("-inf")
min=li[0]
for j in range(1,d):
    if li[j]-min>max:
        max=li[j]-min
    if li[j]<min:
        min=li[j]

print(max)