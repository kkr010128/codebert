# coding: utf-8
# Your code here!
import numpy as np
import math

A,B,H,M=map(int,input().split())

time=(60*H+M)
a=360/720*time
b=360/60*M
c=math.radians(b-a)


print((A**2+B**2-2*A*B*np.cos(c))**0.5)
