N=int(input())
S={}
for n in range(N):
  s=input()
  S[s]=S.get(s,0)+1

maxS=max(S.values())
S=[k for k,v in S.items() if v==maxS]
print('\n'.join(sorted(S)))
