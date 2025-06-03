n=int(input())
G=[[j for j in range(n)] for i in range(n)]
for i in range(n):
    g_in=list(map(int,input().split()))
    u=g_in[0]
    k=g_in[1]
    v=g_in[2:]
    for j in v:
        G[u-1][j-1]=1

visited=[0 for i in range(n)]
finished=[0 for i in range(n)]
L=[]
out=[[i+1,0,0] for i in range(n)]
step=0

def dfs(cn):
    flg=0
    if visited[cn]==0:
        flg=1
        L.append(cn)
    visited[cn]=1
    for i in range(n):
        if cn!=i and G[cn][i]==1 and visited[i]==0:
            dfs(i)
    if flg==1:
        L.append(cn)

i=0
while visited.count(1)<n:
    dfs(i)
    i+=1
copied=[0 for i in range(len(L))]

for i in range(len(L)):
    if copied[L[i]]==0:
        copied[L[i]]=1
        out[L[i]][1]=i+1
    elif copied[L[i]]==1:
        copied[L[i]]=2
        out[L[i]][2]=i+1

out=[' '.join(map(str,i)) for i in out]
#print(' '.join(map(str,[i+1 for i in L])))
print('\n'.join(map(str,out)))
