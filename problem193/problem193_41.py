h,w,K = map(int,input().split())
s = [[int(i) for i in list(input())] for _ in range(h)]

ssum = [[0]*w for _ in range(h)]
for i in range(h):
  for j in range(w):
    if i == 0:
      ssum[i][j] = s[i][j]
    else:
      ssum[i][j] = ssum[i-1][j] + s[i][j]

def cnt(line,i,j):
  if i == 0:
    return ssum[j-1][line]
  else:
    return ssum[j-1][line] - ssum[i-1][line]

ans = 10**6
for i in range(2**(h-1)):
  l = [0]
  s = 0
  for j in range(h):
    if i >> j & 1:
      s += 1
      l.append(j+1)
  l.append(h)
  d = [0]*(len(l)-1)
  for j in range(w):
    nxt = [cnt(j,l[k],l[k+1]) for k in range(len(l)-1)]
    d2 = [nxt[i]+d[i] for i in range(len(l)-1)]
    if max(nxt) > K:
      s = 10**7
      break
    if max(d2) > K:
      d = nxt
      s += 1
    else:
      d = d2
  ans = min(ans,s)
print(ans)