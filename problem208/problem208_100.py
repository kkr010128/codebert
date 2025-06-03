import sys

N, M = map(int, input().split())

S = []
C = []
for m in range(M):
  s, c = map(int, input().split())
  S.append(s)
  C.append(c)

for i in range(10**N):
  tes = str(i)

  if len(tes) != N:
    continue
  
  flag = True
  for s, c in zip(S, C):
    if tes[s-1] != str(c):
      flag = False
  if flag:
    print(tes)
    sys.exit()


print(-1)