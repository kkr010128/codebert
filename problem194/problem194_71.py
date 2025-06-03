from collections import deque
h,w=map(int,input().split())
field=[["*" for i in range(w+2)]]+[["*"]+list(input())+["*"] for i in range(h)]+[["*" for i in range(w+2)]]
cost=[[500 for i in range(w+2)] for j in range(h+2)]
cost[1][1]=0
ans=0
for i in range(1,h+1):
    for j in range(1,w+1):
        color=field[i][j]
        if color=="." and field[i][j+1]=="#":
            cost[i][j+1]=min(cost[i][j]+1,cost[i][j+1])
        else:cost[i][j+1]=min(cost[i][j],cost[i][j+1])
        if color=="." and field[i+1][j]=="#":
            cost[i+1][j]=min(cost[i][j]+1,cost[i+1][j])
        else:cost[i+1][j]=min(cost[i][j],cost[i+1][j])
print(cost[h][w] if field[1][1]=="." else cost[h][w]+1)
