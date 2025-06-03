import numpy as np
import numba
from numba import njit, b1, i4, i8, f8
@njit((i8[:],i8[:],i8[:],i8[:]), cache=True)
def main(lis_h,lis_w,bomb_h,bomb_w):
  bomb = {}
  for h,w in zip(bomb_h,bomb_w):
    bomb[(h,w)] = 1
  m_h = max(lis_h)
  m_w = max(lis_w)
  m_h_lis = []
  m_w_lis = []
  for i,l in enumerate(lis_h):
    if l==m_h:
      m_h_lis.append(i)
  for i,l in enumerate(lis_w):
    if l==m_w:
      m_w_lis.append(i)
  ans = m_h+m_w
  for h in m_h_lis:
    for w in m_w_lis:
      if (h,w) not in bomb:
        return ans
  return ans-1

H, W, M = map(int, input().split())
bombh = np.zeros(M, np.int64)
bombw = np.zeros(M, np.int64)
lis_h = np.zeros(H, np.int64)
lis_w = np.zeros(W, np.int64)
for i in range(M):
    h,w = map(int, input().split())
    h -= 1
    w -= 1
    bombh[i], bombw[i] = h,w
    lis_h[h] += 1
    lis_w[w] += 1
print(main(lis_h,lis_w,bombh,bombw))
