n=int(input())
G=[]
for i in range(n):
    L=list(map(int,input().split()))
    G.append(L[2:])
    for j in range(len(G[-1])):
        G[-1][j]-=1

Forder=[-1]*n
Lorder=[-1]*n
ptr=1
def dfs(v):
    #print(v)
    #print(G[v])
    #print()
    global ptr

    Forder[v]=ptr
    ptr+=1

    for next in G[v]:
        if Forder[next]!=-1:
            continue
        dfs(next)
    
    Lorder[v]=ptr
    ptr+=1

#while True:
#    #print(Forder,Lorder)
#    for i in range(n):
#        if Forder[i]!=-1 and Lorder[i]!=-1:
#            pass
#        else:
#            dfs(i)
#            continue
#
#        if i==n-1:
#            break
#    else:
#        continue
#    break
#
#for i in range(n):
#    print(i+1,Forder[i],Lorder[i])

##########
for i in range(n):
    if Forder[i]==-1 or Lorder[i]==-1:
        dfs(i)

for i in range(n):
    print(i+1,Forder[i],Lorder[i])
