D=int(input())
C=list(map(int,input().split()))
S=list()
for i in range(D):
  S.append(list(map(int,input().split())))
t=list()
for i in range(D):
  t.append(int(input()))

M=0
di=[0]*26
for d in range(D):
  for i in range(26):
    if i==t[d]-1:
      di[i]=0
    else:
      di[i]+=1
  M+=S[d][t[d]-1]
  for i in range(26):
    M-=C[i]*(di[i])
  print(M)