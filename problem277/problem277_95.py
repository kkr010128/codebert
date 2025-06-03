h,w,k = map(int,input().split())
a = [input() for i in range(h)]
c = 1
cou = 1
for i in range(h):
  if '#' not in a[i]:
    cou += 1
  else:
    ans = [c]*(a[i].index('#')+1)
    for j in range(a[i].index('#')+1,w):
      if a[i][j] == '#':
        c += 1
        ans.append(c)
      else:
        ans.append(c)
    [print(*ans) for i in range(cou)]
    break
for i in range(cou,h):
  if '#' not in a[i]:
    print(*ans)
  else:
    c += 1
    ans = [c]*(a[i].index('#')+1)
    for j in range(a[i].index('#')+1,w):
      if a[i][j] == '#':
        c += 1
        ans.append(c)
      else:
        ans.append(c)
    print(*ans)