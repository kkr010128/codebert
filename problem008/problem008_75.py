n=int(input())
#V[u]=[k,[v],d,f]
V=[[0,[],0,0]]
for i in range(n):
    v=[int(i) for i in input().split(" ")]
    u=v.pop(0)
    k=v.pop(0)
    v.sort()
    V.append([k,v,0,0])


def is_finished(Id):
    k=V[Id][0]
    v=V[Id][1]
    for i in range(k):
        if V[v[i]][2]==0:
            return v[i]
    return -1

time=1

while time<=2*n:
 for i in range(1,n+1):
     if V[i][2]==0:
         cur=i
         log=[i]
         break

 while len(log)>0:
    if V[cur][2]==0:
        V[cur][2]=time
        time+=1


    x=is_finished(cur)
    if x!=-1:
        cur=x
        log.append(cur)
    else:
        try:
            log.pop(-1)
            V[cur][3]=time
            time+=1
            if V[cur][3]==V[cur][2]:
                time+=1
                V[cur][3]+=1

            cur=log[-1]
        except:
            pass
for i in range(1,n+1):
    print(i,V[i][2],V[i][3])