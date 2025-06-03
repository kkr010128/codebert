n=int(input())
E=[0]*n
for _ in range(n):
    u,k,*V=map(int,input().split())
    E[u-1]=sorted(V)[::-1]
todo=[1]
seen=[0]*n
d=[0]*n
f=[0]*n
t=0
while 0 in f:
    if not todo:
        todo.append(seen.index(0)+1)    
    if seen[todo[-1]-1]==0:
        seen[todo[-1]-1]=1
        t+=1
        d[todo[-1]-1]=t
        for v in E[todo[-1]-1]:
            if d[v-1]==0:
                todo.append(v)
    elif f[todo[-1]-1]==0:
        t+=1
        f[todo.pop()-1]=t
    else:
        todo.pop()
for i in range(n):
    print(i+1,d[i],f[i])
