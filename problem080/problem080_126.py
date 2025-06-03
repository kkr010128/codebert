# -*- coding: utf-8 -*-


N=int(input())

x,y=map(int,input().split())
R=x
L=x
U=y
B=y

P=[(x,y)]
for i in range(1,N):
    x,y=map(int,input().split())
    P.append((x,y))
    if R<x:R=x
    if L>x:L=x
    if U<y:U=y
    if B>y:B=y

p=P[0]

UR=p
dUR=abs(R-p[0])+abs(U-p[1])
UL=p
dUL=abs(L-p[0])+abs(U-p[1])
BR=p
dBR=abs(R-p[0])+abs(B-p[1])
BL=p
dBL=abs(L-p[0])+abs(B-p[1])

for p in P[1:]:
    if dUR>abs(R-p[0])+abs(U-p[1]):
        UR=p
        dUR=abs(R-p[0])+abs(U-p[1])
    if dUL>abs(L-p[0])+abs(U-p[1]):
        UL=p
        dUL=abs(L-p[0])+abs(U-p[1])
    if dBR>abs(R-p[0])+abs(B-p[1]):
        BR=p
        dBR=abs(R-p[0])+abs(B-p[1])
    if dBL>abs(L-p[0])+abs(B-p[1]):
        BL=p
        dBL=abs(L-p[0])+abs(B-p[1])
    

ans=abs(UR[0]-BL[0])+abs(UR[1]-BL[1])

ans2=abs(UL[0]-BR[0])+abs(UL[1]-BR[1])
if ans2>ans: ans=ans2

print(ans)
