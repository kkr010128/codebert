# coding: utf-8
import math
import numpy as np
#N = int(input())
#A = list(map(int,input().split()))
x = int(input())
#x, y = map(int,input().split())
for i in range(1,10**5):
    if (i*x)%360==0:
        print(i)
        break