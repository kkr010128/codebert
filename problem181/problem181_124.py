k = int(input())
cur = [[1]*10 for i in range(11)]
if k <= 9:
  print(k)
  exit()
c = 9
i = 0
while c < k:
  i += 1
  for j in range(10):
    cur[i][j] = cur[i-1][j]
    if j != 0:
      cur[i][j] += cur[i-1][j-1]
    if j != 9:
      cur[i][j] += cur[i-1][j+1]
  if c+sum(cur[i][1:]) >= k:
    break
  else:
    c += sum(cur[i][1:])
ans = ''
for j in range(i,-1,-1):
  for l in range(10):
    if j == i and l == 0:
      continue
    if j != i and abs(l-int(ans[-1])) > 1:
      continue
    if c + cur[j][l] >= k:
      ans += str(l)
      break
    else:
      c += cur[j][l]
print(ans)