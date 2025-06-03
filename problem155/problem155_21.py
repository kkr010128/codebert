n,m = map(int,input().split())
h = list(map(int,input().split()))
nf = [1] * n
for i in range(m):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  if h[a] > h[b]:
    nf[b] = 0
  elif h[a] < h[b]:
    nf[a] = 0
  else:
    nf[a] = 0
    nf[b] = 0
print(nf.count(1))