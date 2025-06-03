   #depth first
N=int(input())
V=[]
a=[0]
for i in range(N):
    V.append([int(i) for i in input().split()])
    w=V[i][2:]
    w.sort()
    V[i]=V[i][:2]+w
    a.append(0)
V=sorted(V,key=lambda x:x[0])
c=1
t=1
i=0
r=[1]
a[1]=1
p=[[1,t]]
q=[]
while t<N*2:
    j=2
    while t<N*2 and j-2<V[i][1] and V[i][1]>0 and a[V[i][j]]==1:
        j+=1
    t+=1
    if j-2<V[i][1]:
        a[V[i][j]]=1
        c+=1
        r.append(V[i][j])
        p.append([V[i][j],t])
        i=V[i][j]-1
    else:
        q.append(p[-1]+[t])
        r.pop(-1)
        p.pop(-1)
        if len(r)>0:
            i=r[-1]-1
        else:
            j=1
            while j<N and a[j]==1:
                j+=1
            if j<N:
                t+=1
                i=j-1
                r.append(j)
                p.append([j,t])
q=sorted(q,key=lambda x:x[0])
for i in range(N):
    for j in range(3):
        q[i][j]=str(q[i][j])
    print(" ".join(q[i]))