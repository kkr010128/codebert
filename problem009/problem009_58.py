from collections import deque
Q=deque()
n=int(input())
graph={}
d=[0 for i in range(n+1)]

for i in range(n):
    tmp=list(map(int,input().split()))
    graph[tmp[0]]=[0 for j in range(n+1)]
    for j in range(tmp[1]):
        graph[tmp[0]][tmp[2+j]]=1

Q.append(1)
while len(Q) is not 0:
    number=Q[0]
    if 1 in graph[number]:
        for i in range(graph[number].count(1)):
            Q.append(graph[number].index(1))
            if d[graph[number].index(1)] is 0:
                d[graph[number].index(1)]=d[number]+1
            graph[number][graph[number].index(1)]=0
        
    Q.popleft()

for i in range(n):
    if i==0:
        print(i+1,0)
    else:
        if d[i+1]==0:
            print(i+1,-1)
        else:
            print(i+1,d[i+1])
