from itertools import product
import copy
H,W,K = list(map(int, input().split()))
A = []
for i in range(H):
  A.append(list(map(int, input())))

#SM = [np.cumsum(A[i]) for i in range(H)]

ANS = []
for pat in product(['0','1'], repeat = H-1):
  res = []
  cnt = 0
  now = copy.copy(A[0])
  for i in range(1,H):
    p = pat[i-1]
    if p == '1':
      res.append(now)
      now = copy.copy(A[i])
      cnt += 1
    else:
      for j in range(W):
        now[j] += A[i][j]
  res.append(now)
  
  """  
  print("---")
  print(pat)
  print(res)
  print(cnt)
  """  
  wk2 = [0] * len(res)
  cnt2 = 0
  flg = True
  for x in range(W):
    for j in range(len(res)):
      if res[j][x] > K:
        # 横に割った段階で、すでに最小単位がKを超えてたら実現不可能
        flg = False
        break
      if wk2[j] + res[j][x] > K:
        cnt2 += 1
        wk2 = [0] * len(res)
        break
    for j in range(len(res)):
      wk2[j] += res[j][x]
    if not flg:
      break
      
  if flg:
    ANS.append(cnt + cnt2)
    #print(pat, cnt, cnt2)
print(min(ANS))
