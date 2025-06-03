N,M=list(map(int,input().split()))
E={i:[] for i in range(1,N+1)}
for i in range(M):
    a,b=list(map(int,input().split()))
    E[a].append(b)
    E[b].append(a)
V={i:0 for i in range(1,N+1)}
W=[1]
while W!=[]:
    S=[]
    for a in W:
        for b in E[a]:
            if V[b]==0:
                V[b]=a
                S.append(b)
    W=S
if -1 in V:
    print('No')
else:
    print('Yes')
    for i in range(2,N+1):
        print(V[i])