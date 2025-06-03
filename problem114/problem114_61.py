N = 26
D = int(input())
C = [int(i) for i in input().split()]

S = []
for i in range(D):
  s = [int(i) for i in input().split()]
  S.append(s)
  
SUM = 0
L = [0] * 26
  
T = []
for i in range(D):
  t = int(input())
  T.append(t-1)

for i in range(D):
  d = i + 1
  for j in range(N):
    if j == T[i]:
      SUM += S[i][j]
      L[j] = d
    else:
   	  SUM -= C[j] * (d - L[j])
  else:
    print(SUM)
