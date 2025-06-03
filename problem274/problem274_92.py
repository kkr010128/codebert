import sys
N,M=map(int,input().split())
S=input()
lst=[]
koma=N
rs=0
ME=0
pn=0
while koma>0 and pn==0:
 rs+=1
 if int(S[koma-rs])==0:
  ME=rs
 if koma-rs==0 or rs==M:
  lst.append(ME)
  if ME==0:
   pn+=1
  koma-=ME
  rs=rs-ME
  ME=0
if pn>0:
 print(-1)
else:
 lst.reverse()
 print(*lst)
