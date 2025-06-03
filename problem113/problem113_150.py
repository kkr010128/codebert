def yumiri(L, n):
  for i in range(len(L)):
    if L[i] > n:
      return i - 1

def parunyasu(a, b, p, q):
  reans = ans
  rd1, rq1, d1, nd1, nq1, q1, newans = naobou(a, q, reans)
  rd2, rq2, d2, nd2, nq2, q2, newans = naobou(b, p, newans)

  if reans <= newans:
    t[d1 - 1] = q1
    t[d2 - 1] = q2
    return newans
  else:
    ayaneru(rd2, rq2, d2, nd2, nq2)
    ayaneru(rd1, rq1, d1, nd1, nq1)
    return reans

def ayaneru(rd, rq, d, nd, nq):
  ZL[rd].insert(rq, d)
  del ZL[nd][nq + 1]

def naobou(d, q, ans):
  newans = ans

  rd = t[d - 1] - 1
  rq = yumiri(ZL[rd], d)
  newans += SUMD[ZL[rd][rq] - ZL[rd][rq - 1] - 1] * c[rd]
  newans += SUMD[ZL[rd][rq + 1] - ZL[rd][rq] - 1] * c[rd]
  newans -= SUMD[ZL[rd][rq + 1] - ZL[rd][rq - 1] - 1] * c[rd] 
  del ZL[rd][rq]

  nd = q - 1
  nq = yumiri(ZL[nd], d)
  newans += SUMD[ZL[nd][nq + 1] - ZL[nd][nq] - 1] * c[nd]
  newans -= SUMD[d - ZL[nd][nq] - 1] * c[nd]
  newans -= SUMD[ZL[nd][nq + 1] - d - 1] * c[nd]
  ZL[nd].insert(nq + 1, d)

  newans -= s[d - 1][rd]
  newans += s[d - 1][nd]

  return rd, rq, d, nd, nq, q, newans

def rieshon():
  ans = 0
  for i in range(D):
    ans += s[i][t[i] - 1]
    for j in range(26):
      if t[i] - 1 == j:
        L[j] = 0
        ZL[j].append(i + 1)
      else:
        L[j] += 1
        ans -= L[j] * c[j]
  for i in range(26):
    ZL[i].append(D + 1)
  return ans

import time
import random
startTime = time.time()

D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]

L = [0] * 26
ZL = [[0] for _ in range(26)]
SUMD = [0] * (D + 1)
for i in range(1, D + 1):
  SUMD[i] = SUMD[i - 1] + i

RD = [0] * 26
t = [0] * D
for i in range(D):
  RD[0] += 1
  ma = s[i][0] + RD[0] * c[0]
  man = 0
  for j in range(1, 26):
    RD[j] += 1
    k = s[i][j] + RD[j] * c[j]
    if k > ma:
      ma = k
      man = j
  t[i] = man + 1
  RD[man] = 0

ans = rieshon()
while time.time() - startTime < 1.8:
  l = random.randrange(min(D - 1, 13)) + 1
  d = random.randrange(D - l) + 1
  p = t[d - 1]
  q = t[d + l - 1]
  if p == q: continue
  ans = parunyasu(d, d + l, p, q)

for i in range(D):
  print(t[i])
