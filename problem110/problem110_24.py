row, col, num = map(int, input().split())

tmp_l = []
board = []
for i in range(row):
  str = input()
  for j in range(col):
    if str[j] == '.':
      tmp_l.append(0)
    if str[j] == '#':
      tmp_l.append(1)
  board.append(tmp_l)
  tmp_l = []

onoff = []
bi = [32, 16, 8, 4, 2, 1]
for i in range(64):
  tmp = i
  for j in bi:
    tmp_l.insert(0, int(tmp / j))
    tmp %= j
  onoff.append(tmp_l)
  tmp_l = []

count = 0
ans = 0
for i in range(2**row):
  for j in range(2**col):
    for k in range(row):
      if onoff[i][k] == 1:
        for l in range(col):
          if onoff[j][l] == 1:
            if board[k][l] == 1:
              count += 1
    if count == num:
      ans += 1
    count = 0

print(ans)