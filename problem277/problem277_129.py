h,w,k = map(int,input().split())
s = [list(input()) for i in range(h)]
a = [[0]*w for i in range(h)]
num = 1
for i in range(h):
  b = s[i]
  if "#" in b:
    t = b.count("#")
    for j in range(w):
      c = b[j]
    #  print(c)
      if c=="#" and t!=1:
        a[i][j] = num
        num += 1
        t -= 1
      elif c=="#" and t==1:
        a[i][j] = num
        t = -1
      else:
        a[i][j] = num
    if t==-1:
      num += 1
  else:
    if i==0:
      continue
    else:
      for j in range(w):
        a[i][j] = a[i-1][j]
index = 0

for i in range(h):
  if "#" not in s[i]:
    index += 1
  else:
    break
for j in range(index):
  for k in range(w):
    a[j][k] = a[index][k]
for j in a:
  print(*j)