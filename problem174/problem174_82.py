import math
import numpy as np
k = int(input())

Map = [[0 for j in range(k)] for i in range(k)]
for i  in range(1,k+1):
    for j in range(1,k+1):
        tmp = math.gcd(i,j)
        Map[i-1][j-1] = tmp
        Map[j-1][i-1] = tmp

ans = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        tmp_ans = Map[i-1][j-1]
        for x in range(1,k+1):
            ans += Map[tmp_ans-1][x-1]
            
            
print(ans)
