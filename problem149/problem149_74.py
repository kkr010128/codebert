import sys
def hantei(N,M,X,A,l):
  skill = [0] * M
  money = 0
  for i in range(N):
    if l[i] == '1':
      money += A[i][0]
      for j in range(M):
        skill[j] += A[i][j+1]
  for k in skill:
    if k < X:
      return -1
      sys.exit()
  return money
      
N,M,X = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
mny = 12 * (10 ** 5) + 1
for i in range(1,2**N):
  l = bin(i)[2:].zfill(N)
  if hantei(N,M,X,A,l) != -1 and hantei(N,M,X,A,l) < mny:
    mny = hantei(N,M,X,A,l)
    a = l
if mny == 12 * (10 ** 5) + 1:
  print(-1)
else:
  print(mny)