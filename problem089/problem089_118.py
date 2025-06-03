import numpy as np
H,W,M = map(int,input().split())
#h = np.empty(M,dtype=np.int)
#w = np.empty(M,dtype=np.int)
bomb = set()
hh = np.zeros(H+1,dtype=np.int)
ww = np.zeros(W+1,dtype=np.int)

for i in range(M):
    h,w = map(int,input().split())
    bomb.add((h,w))
    hh[h] += 1
    ww[w] += 1

#print(bomb)
h_max = np.max(hh)
w_max = np.max(ww)

h_max_ids = list()
w_max_ids = list()
for i in range(1,H+1):
    if hh[i] == h_max:
      h_max_ids.append(i)
for j in range(1,W+1):
    if ww[j] == w_max:
      w_max_ids.append(j)
      
for i in h_max_ids:
  for j in w_max_ids:
    if not (i,j) in bomb:
      print(h_max + w_max)
      exit()

#print("hmax:{} wmax:{}".format(h_max_id, w_max_id))
#print("hmax:{} wmax:{}".format(hh[h_max_id], ww[w_max_id]))
print(h_max + w_max - 1)
