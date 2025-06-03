n,m = map(int,input().split())
*hl, = map(int,input().split())
ansl = [1]*n
for _ in [0]*m:
  a,b = map(int,input().split())
  if hl[a-1] > hl[b-1]:
    ansl[b-1] = 0
  elif hl[a-1] < hl[b-1]:
    ansl[a-1] = 0
  else:
    ansl[a-1] = 0
    ansl[b-1] = 0
print(sum(ansl))