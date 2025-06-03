def DFS(num):
    global time
    time +=1
    color[num]="gray"
    D[num][0]=time
    for i in M[num]:
        if color[i]=="white":
            DFS(i)
    color[num]="black"
    time +=1
    D[num][1]=time


n=int(input())
M=[[] for _ in range(n+1)]
for i in range(n):
    for j in list(map(int,input().split()))[2:]:
        M[i+1].append(j)
color=["white" for _ in range(n+1)]
D=[[0,0] for _ in range(n+1)]
time=0
for i in range(n):
    if color[i+1]=="white":
        DFS(i+1)

for i in range(n):
    print(i+1,*D[i+1])
