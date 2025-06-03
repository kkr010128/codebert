N = int(input())
A = list(map(int, input().split()))
D = {a:0 for a in set(A)}
for a in A:
  D[a] += 1
S = 0
for v in D.values():
  if v>=2:
    S += v*(v-1)//2
for a in A:
  d = D[a]
  if d==1:
    print(S)
  else:
    print(S-d*(d-1)//2+(d-1)*(d-2)//2)