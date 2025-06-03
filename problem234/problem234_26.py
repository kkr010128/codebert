import math
import numpy as np
N = int(input())
tb = [[0]*10]*10
tb = np.array(tb)
for i in range(1,N+1):
    s = str(i)
    tb[int(s[0])][int(s[-1])] =tb[int(s[0])][int(s[-1])] +1
 
point =0
 
for i in range(0,10):
    for j in range(0,10):
        point += tb[i][j] * tb[j][i]
 
print(point)