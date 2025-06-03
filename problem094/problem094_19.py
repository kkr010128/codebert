import sys
import numpy as np
from numba import njit,i8

R,C,K = map(int,input().split())
item = np.zeros((R,C),np.int64)
for _ in range(K):
    r,c,v = map(int,input().split())
    item[r-1][c-1] = v
    

@njit(i8(i8[:,:],i8,i8), cache = True)
def solve(item,R,C):
    dp = np.zeros((R+1,C+1,4),np.int64)
    for ri in range(R):
        for ci in range(C):
            dp[ri+1][ci+1][0] = max(dp[ri+1][ci][0], dp[ri][ci+1][3])
            dp[ri+1][ci+1][1] = max(dp[ri+1][ci][1], dp[ri+1][ci][0]+item[ri][ci], dp[ri][ci+1][3]+item[ri][ci], dp[ri+1][ci+1][0])
            dp[ri+1][ci+1][2] = max(dp[ri+1][ci][2], dp[ri+1][ci][1]+item[ri][ci], dp[ri+1][ci+1][1])
            dp[ri+1][ci+1][3] = max(dp[ri+1][ci][3], dp[ri+1][ci][2]+item[ri][ci], dp[ri+1][ci+1][2])
        

    return dp[-1][-1][3]

print(solve(item,R,C))