import itertools
N = int(input())
z = []
for i in range(N):
  x,y = map(int,input().split())
  z.append((x,y))
ALL = 1
for i in range(N):
  ALL *= (i+1)
base = [i for i in range(N)]
A = list(itertools.permutations(base,N))
SUM = 0

def distance(a,b):
  ax = a[0]; ay = a[1]
  bx = b[0]; by = b[1]
  dis = ((ax-bx)**2 + (ay-by)**2)**(0.5)
  return dis

for X in A:
  now = z[X[0]]
  for i in range(1,N):
    nxt = z[X[i]]
    dif = distance(now,nxt)
    #print(dif)
    SUM += dif
#print(SUM,ALL)
ans = SUM/ALL
print(ans)