import numpy as np
N,M = map(int, input().split())
H = np.array(list(map(int, input().split())))
box = [[] for _ in range(N)]
for im in range(M):
  a,b = map(int, input().split())
  box[a-1].append(b)
  box[b-1].append(a)
ans = 0
for n in range(N):
  index=np.array(box[n],dtype=int)-1
  if len(index)==0:
    ans += 1
    continue
  if H[n]>np.max(H[index]):
    ans += 1
print(ans)