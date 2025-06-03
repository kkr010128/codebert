N = int(input())
L = [0]
M = list(range(1 , N + 1))
a = 1
for i in range(1 , N):
  for j in range(1 ,i + 1):
    a = a * j
  L.append(a)
  a = 1
list.sort(L,reverse = True)
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
con_P = 0
con_Q = 0
for k in range(0 , N - 1):
  if k != N - 2:
    con_P += L[k] * (M.index(P[k]))
    M.remove(P[k])
  else:
    con_P += L[k] * (M.index(P[k]) + 1)
    
M = list(range(1 , N + 1))

for l in range(0 , N - 1):
  if l != N - 2:
    con_Q += L[l] * (M.index(Q[l]))
    M.remove(Q[l])
  else:
    con_Q += L[l] * (M.index(Q[l]) + 1)
ans = con_P - con_Q
if ans < 0:
  print(-ans)
else:
  print(ans)

