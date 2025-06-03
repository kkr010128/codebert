#ARC162 C:Sum of gcd of Tuples(Easy)
import math
import numpy as np
import itertools
k = int(input())
ans = 0

if k == 1:
    ans = 1
else:
    for i in range(1,k+1):
        for j in range(1,k+1):
            a = math.gcd(i,j)
            for k in range(1,k+1):
                b = math.gcd(a,k)
                ans += b    
print(ans)