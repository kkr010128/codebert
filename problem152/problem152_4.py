N = int(input())
S = [input() for _ in range(N)]

D = [[0] * 2 for _ in range(N)]

for i in range(N):
  s = S[i]
  ma = 0
  l = 0
  r = 0
  for j in s:
    if j == ")":
      r += 1
    else:
      l += 1
    ma = max(ma, r - l)
  D[i] = [l - r, ma, s]

cnt = 0
P = []
M = []
for x, y ,s in D:
  if x >= 0:
    if y <= 0:
      cnt += x
    else:
      P.append([x, y])
  else:
    M.append([x, y, s])

P.sort(key = lambda x:x[1])

for x, y in P:
  if y > cnt:
    print("No")
    exit()
  cnt += x

if len(M) == 0:
  if cnt == 0:
    print("Yes")
  else:
    print("No")
  exit()

M.sort(reverse = True)
M.sort(key = lambda x:x[1], reverse = True)

for i in range(len(M)):
  x, y, s = M[i]
  if x == -y:
    g = x
    M[i] = [0, 0, ""]
    break
else:
  print("No")
  exit()

for x, y, s in M:
  if cnt < y:
    print("No")
    exit()
  cnt += x

if cnt + g == 0:
  print("Yes")
else:
  print("No")
