from collections import deque
N=int(input())
color=["w"]*(N+1)
start=[None]*(N+1)
finish=[0]*(N+1)
rinsetu=[[] for i in range(N+1)]
for i in range(1,N+1):
    a=list(map(int,input().split()))
    a=a[2:]
    rinsetu[i]=a
def dfs(i,t):
    if color[i]=="w":
        t+=1
        start[i]=t
        color[i]="g"
        for j in rinsetu[i]:
            t=dfs(j,t)
        t+=1
        finish[i]=t
        return t
    else:return t
t=dfs(1,0)
while(None in start[1:]):
    a=start[1:].index(None)
    t=dfs(a+1,t)

for i in range(1,N+1):
    print("%d %d %d" %(i,start[i],finish[i]))

