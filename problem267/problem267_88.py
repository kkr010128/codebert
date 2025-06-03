N=int(input())
s=list(input())
S=[0]*N
for i in range(N):
  S[i]=int(s[i])
ct=0
for i in range(10):
  if not i in S:
    continue
  T=S[S.index(i)+1:]
  for j in range(10):
    if not j in T:
      continue
    U=T[T.index(j)+1:]
    for k in range(10):
      if k in U:
        ct+=1
print(ct)