import numpy as np
n,m=map(int, input().split())
AC=[0]*(n+1)
WA=[0]*(n+1)
for _ in range(m):
   p,s=input().split()
   if s=='AC':
        AC[int(p)]=1
   elif s=='WA' and AC[int(p)]==0:
        WA[int(p)] +=1
        
ACn=np.array(AC)
WAp=np.array(WA)

print(sum(AC),sum(ACn*WAp))