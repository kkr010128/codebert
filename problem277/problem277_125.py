h,w,k = map(int, input().split())
s = []
st = 0
zero = [0 for i in range(h)]
z = 0
for i in range(h):
  t = input()
  st += t.count('#')
  zero[i] = t.count('#')
  s.append(t)

cake = 0
ans = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
  if zero[i] == 0:
    continue
  cake += 1
  t = 0
  for j in range(w):
    if s[i][j] == '#':
      t += 1
      if t >= 2:
        cake += 1
    ans[i][j] = cake
for i in range(h-1):
  if zero[i+1] != 0:
    continue
  if ans[i][0] == 0:
    continue
  for j in range(w):
    ans[i+1][j] = ans[i][j]
for i in range(h-1,0,-1):
  if zero[i-1] != 0:
    continue
  for j in range(w):
    ans[i-1][j] = ans[i][j]

for i in range(h):
  print (*ans[i])