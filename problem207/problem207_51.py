bingo = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
for _ in range(N):
  b = int(input())
  for i in range(3):
    for j in range(3):
      if bingo[i][j] == b:
        bingo[i][j] = 0

ans = "No"
for k in range(3):
  if bingo[k][0] == bingo[k][1] == bingo[k][2] or \
     bingo[0][k] == bingo[1][k] == bingo[2][k]:
    ans = "Yes"
    break
if bingo[0][0] == bingo[1][1] == bingo[2][2] or \
   bingo[0][2] == bingo[1][1] == bingo[2][0]:
  ans = "Yes"
print(ans)