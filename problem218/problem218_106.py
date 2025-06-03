N=int(input())
S={}
for n in range(N):
  s=input()
  S[s]=S.get(s,0)+1

maxS=max(S.values())
S={k:v for k, v in S.items() if v==maxS}
S=sorted(S.items(), key=lambda x:(-x[1],x[0]))
for k,cnt in S:
  print(k)
