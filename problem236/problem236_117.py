H=int(input())
W=int(input())
N=int(input())

cnt=0
black=0
if H>=W:
  for i in range(W):
    black+=H
    cnt+=1
    if black>=N:
      break
elif H<W:
  for i in range(H):
    black+=W
    cnt+=1
    if black>=N:
      break
print(cnt)