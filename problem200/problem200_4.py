a,b,m = map(int,input().split())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))
disc = [[]]*m
for i in range(m):
  disc[i] = list(map(int,input().split()))
mina = 100000
minb = 100000
for i in range(a):
  mina = min(mina,al[i])
for i in range(b):
  minb = min(minb,bl[i])
total = mina+minb
for i in range(m):
  total = min(total,al[disc[i][0]-1]+bl[disc[i][1]-1]-disc[i][2])
print(total)