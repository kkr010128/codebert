N=int(input())
S=[input() for i in range(N)]
L=dict()
for i in range(N):
  if S[i] in L:
    L[S[i]]+=1
  else:
    L[S[i]]=1
M=max(L.values())
ans=list()
for X in L:
  if L[X]==M:
    ans.append(X)
ans.sort()
for X in ans:
  print(X)
