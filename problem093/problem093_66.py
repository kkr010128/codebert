import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

@njit((i8,i8,i8[:],i8[:]), cache=True)
def main(N,K,P,C):
  INF = 1<<30
  ans = -INF
  for i in range(N):
    score = 0
    now = i
    visited = np.full(N,-1,np.int64)
    scores = np.zeros(N,np.int64)
    visited[now] = 0
    for j in range(1,K+1):
      now = P[now]
      score += C[now]
      ans = max(ans, score)
      if visited[now]>=0:
        cyc = j - visited[now]
        up = score - scores[now]
        break
      scores[now] = score
      visited[now] = j
    else:
      continue
    if up<=0:
      continue
    cnt = j+1
    if K-cyc>=j:
      score += (K-cyc-j)//cyc * up
      ans = max(ans, score)
      cnt += (K-cyc-j)//cyc*cyc
    for j in range(cnt,K+1):
      now = P[now]
      score += C[now]
      ans = max(ans, score)
  return ans

N, K = map(int, input().split())
P = np.array(list(map(lambda x:int(x)-1, input().split())))
C = np.array(list(map(int, input().split())))

print(main(N,K,P,C))