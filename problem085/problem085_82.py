#ABC177E
N = int(input())
#N = 1000000
A = list(map(int, input().split()))
#A = [i+1 for i in range(1000000)]
p = {2*i+1: 1 for i in range(1, 500)}
for i in range(3, 1000, 2):
  for j in p:
    if j != i:
      if j % i == 0:
        p[j] = 0
L = [2]
for i in p:
  if p[i] == 1:
    L.append(i)
def gcd(x, y):
  k, l = x, y
  while l:
    k, l = l, k % l
  return k
g = A[0]
i = 0
nn = len(L)
while i < N:
  g = gcd(g, A[i])
  if g == 1:
    break
  i += 1
if g > 1:
  print("not coprime")
else:
  D = {}
  m = 0
  for i in A:
    pnt = 0
    x = i
    for j in L:
      cnt = False
      while x % j == 0:
        cnt = True
        x //= j
      if cnt:
        if j in D:
          D[j] += 1
          if D[j] == 2:
            m = 2
            break
        else:
          D[j] = 1
      pnt += 1
      if pnt == nn and x != 1:
        if x in D:
          D[x] += 1
          if D[x] == 2:
            m = 2
        else:
          D[x] = 1
        break
      if x == 1:
        break
    if m >= 2:
      break
  if D == {}:
    print("pairwise coprime")
  else:
    if m > 1:
      print("setwise coprime")
    else:
      print("pairwise coprime")