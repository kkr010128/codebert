H,V,M=map(int,input().split())
h=[0 for i in range(M)]
w=[0 for i in range(M)]
for i in range(M):
    h[i],w[i]=map(int,input().split())
Dh=dict()
Dw=dict()
for i in range(M):
    if h[i] in Dh:
        Dh[h[i]]+=1
    else:
        Dh[h[i]]=1
    if w[i] in Dw:
        Dw[w[i]]+=1
    else:
        Dw[w[i]]=1
Hmax=0
Wmax=0
for i in Dh:
    if Dh[i]>Hmax:
        Hmax=Dh[i]
for i in Dw:
    if Dw[i]>Wmax:
        Wmax=Dw[i]
A=0
B=0
for i in Dh:
    if Dh[i]==Hmax:
        A+=1
for i in Dw:
    if Dw[i]==Wmax:
        B+=1
tmp=0
for i in range(M):
    if Dh[h[i]]==Hmax and Dw[w[i]]==Wmax:
        tmp+=1
if A*B>tmp:
    print(Hmax+Wmax)
else:
    print(Hmax+Wmax-1)
