import sys,io,os
z=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
y=lambda:map(int,z().split())
n,m=y()
k={}
p={}
r=0
e=0
def path(r):
    while p[r]>=0:r=p[r]
    return r
for i in range(m):
    a,b=y();a-=1;b-=1;e+=1
    if a in k:
        if b in k:
            va,vb=path(k[a]),path(k[b])
            if va>vb:p[va]=vb
            elif va<vb:p[vb]=va
            else:e-=1
        else:k[b]=k[a]
    else:
        if b in k:k[a]=k[b]
        else:
            k[a]=r
            k[b]=r
            p[r]=-1
            r+=1
print(n-1-e)