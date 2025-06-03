import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

@njit((i8, i8, i8, i8[:,:]), cache=True)
def solve(R,C,K,item):
  dp = np.zeros((C+1,5), dtype=np.int64)
  for i in range(1,R+1):
    new_dp = np.zeros((C+1,5), dtype=np.int64)
    #上からアイテムを取らずに移動
    new_dp[:,0] = dp[:,-1]
    #上からアイテムを取って移動
    new_dp[1:,1] = np.maximum(new_dp[1:,1],dp[1:,-1]+item[i-1])
    for j in range(1,C+1):
      #横からアイテムを取らずに移動
      new_dp[j] = np.maximum(new_dp[j],new_dp[j-1])
      #横からアイテムを取って移動
      for k in range(1,4):
        new_dp[j,k] = max(new_dp[j,k],new_dp[j-1,k-1]+item[i-1,j-1])
    for k in range(4):
      new_dp[:,-1] = np.maximum(new_dp[:,-1],new_dp[:,k])
    dp = new_dp
  ans = dp[-1,-1]
  return ans

R, C, K = map(int, input().split())
item = np.zeros((R,C), dtype=np.int64)
for i in range(K):
  r,c,v = map(int, input().split())
  item[r-1,c-1] = v
print(solve(R,C,K,item))