import math
import numpy as np
A,B = np.array(input().split(),dtype = int)

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

print(int(A*B/(gcd(A,B))))