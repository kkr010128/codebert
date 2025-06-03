N,M = map(int,input().split())
AC = N*[0]
WA = N*[0]

for m in range(M):
  P,S = input().split()
  P = int(P)-1
  
  if AC[P]==1:
    continue
  if S=="WA":
    WA[P]+=1
  else:
    AC[P]=1

wa = 0 
for a,w in zip(AC,WA):
  wa+=w*a

print(sum(AC),wa)