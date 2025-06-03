import itertools
H,W,K = map(int,input().split())
S = []
for i in range(H):
  s= map(int,input())
  S.append(list(s))
l = list(itertools.product([0,1], repeat=H-1))
l = [list(li) for li in l]
for i in range(len(l)):
  l[i] = [j+1 for j in range(len(l[i])) if l[i][j] > 0]
  
S_t = [list(x) for x in zip(*S)]
for i in range(W):
  for j in range(1,H):
    S_t[i][j] += S_t[i][j-1]
flag = False  
min_cnt = H*W
for i in range(len(l)):
  cnt = 0
  bh = [0]+[li  for li in l[i] if li > 0]+[H]
  white = [0]*(len(bh)-2+1)
  j = 0
  while j < W:
    if flag == True:
      white = [0]*(len(bh)-2+1)
      cnt += 1
      flag = False
    for k in range(len(bh)-1):
      if bh[k] == 0:
        su = S_t[j][bh[k+1]-1]
      else:
        su = S_t[j][bh[k+1]-1]-S_t[j][max(0,bh[k]-1)]
      if white[k] + su > K:
        if su > K:
          j = W
          cnt = H*W+1
          flag = False
        else:
          flag = True
        break
      white[k] += su
    if flag == False:
      j += 1
  min_cnt = min(cnt+len(bh)-2,min_cnt)
  
print(min_cnt)
    
      

    
