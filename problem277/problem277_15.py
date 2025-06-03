H,W,K=map(int,input().split())
S=[input() for _ in range(H)]

ans=[[0]*W for _ in range(H)]

zero = -1
count = 1
for i in range(H):
  if zero == -1 and S[i].count('#')==0:
    zero = i
    continue
  if zero != -1 and S[i].count('#')==0:
    continue
  last=0
  for j in range(W):
    if S[i][j]=='.':
      if zero != -1:
        for k in range(zero,i):
          ans[k][j] = count
      ans[i][j] = count
    if S[i][j]=='#':
      if zero != -1:
        for k in range(zero,i):
          ans[k][j] = count
      ans[i][j] = count
      if j<W-1 and S[i][j+1:].count('#')==0:
        last = 1
      else:
        count += 1
    if j == W-1 and last:
      last = 0
      count += 1
    if j == W-1:
      zero = -1
      
if zero != -1:
  for i in range(zero,H):
    ans[i] = ans[zero-1]
      
for i in range(H):
  print(*ans[i])