a = [int(s) for s in input().split()]
N = a[0]
bks = a[1]
bd = a[2]

s = [input().split() for i in range(N)]
anslist = []
for i in range(2**N):
  templist = []
  for t in range(bks+1):
    templist.append(int(0))
  for j in range(N):
    if (i >> j) & 1 == 1:
      for k in range(bks + 1):
        templist[k] += int(s[j][k])
  anslist.append(templist)

ans = int(-1)
flag = int(0)
for i in range(2**N):
  flag = 0
  for j in range(1, bks+1):
    if anslist[i][j] < bd:
      flag = 1
      break
    else:
      pass
  if flag == 0:
      if anslist[i][0] < ans or ans == -1:
        ans = anslist[i][0]

print(ans)