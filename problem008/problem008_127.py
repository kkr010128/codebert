global graph
global seen
token=0

def dfs(i):
    global token
    token+=1
    seen[i][0]=token
    for x in graph[i]:
        if seen[x][0]==0:
            dfs(x)
    token+=1
    seen[i][1]=token


n=int(input())

graph=[None for _ in range(n+1)]

for i in range(n):
    lst=list(map(int,input().split()))
    graph[lst[0]]=lst[2:]

seen=[[0,0] for _ in range(n+1)]

for i in range(1,n+1):
    if seen[i][0]==0:
        dfs(i)

for i in range(1,n+1):
    print("{} {} {}".format(i,seen[i][0],seen[i][1]))
