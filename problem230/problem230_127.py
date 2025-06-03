import math
N,D,A = map(int,input().split())
l = []
for i in range(N):
  l.append(list(map(int,input().split())))
l.sort()  
lx = []
lc = []
for i in l:
  X,H = i[0],i[1]
  lx.append(X)
  lc.append(math.ceil(H/A))

migi = []
m = 0
i = 0
while i <= N-1:
  if lx[m] - lx[i] > 2*D:
    migi.append(m)
    i += 1
  elif m != N-1:
    m += 1
  elif m == N-1:
    migi.append(-1)
    i += 1 

cnt = 0
dam = [0 for i in range(N)]
for i in range(N):
  if dam[i] < lc[i]:
    c = lc[i] - dam[i]  
    dam[i] += c
    if migi[i] >= 0:
      dam[migi[i]] -= c
    cnt += c
  if i <=N-2:
    dam[i+1] += dam[i]   
print(cnt)