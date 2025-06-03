A = [[int(x) for x in input().split()] for _ in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

Bingo = [[0, 0, 0] for _ in range(3)] 
for i in range(3):
  for j in range(3):
    for l in range(N):
      if(A[i][j] == b[l]):
        Bingo[i][j] = 1
bingo = 0
for i in range(3):
  if(Bingo[i][0]+Bingo[i][1]+Bingo[i][2])==3:
    bingo += 1
  elif(Bingo[0][i]+Bingo[1][i]+Bingo[2][i])==3:
    bingo += 1
if(Bingo[0][0]+Bingo[1][1]+Bingo[2][2])==3:
  bingo += 1
elif(Bingo[0][2]+Bingo[1][1]+Bingo[2][0])==3:
  bingo += 1

if(bingo!=0):
  print('Yes')
else:
  print('No')