from collections import deque
n=int(input())
E=[0]*n
for _ in range(n):
    u,k,*V=map(int,input().split())
    E[u-1]=V
d=[-1]*n
d[0]=0
todo=deque([1])
while todo:
    now=todo.popleft()
    for v in E[now-1]:
        if d[v-1]==-1:
            todo.append(v)
            d[v-1]=d[now-1]+1
for i in range(n):
    print(i+1,d[i])
