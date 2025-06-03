# import matplotlib.pyplot as plt
import math
 
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y
 
   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1
 
   return lcm

X = int(input())
print(int(lcm(X, 360) / X))