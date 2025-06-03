N=int(input())
S={}
for n in range(N):
  s=input()
  S[s]=S.get(s,0)+1
  
S=sorted(S.items(), key=lambda x:(-x[1],x[0]))
maxS=S[0][1]
for s, cnt in S:
  if cnt!=maxS:
    break
  print(s)