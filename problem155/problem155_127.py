number=list(map(int,input().split()))
n,m=number[0],number[1]
height=list(map(int,input().split()))
load=[[] for i in range(n+1)]
for i in range(m):
    tmp=list(map(int,input().split()))
    if tmp[1] not in load[tmp[0]]:
        load[tmp[0]].append(tmp[1])
    if tmp[0] not in load[tmp[1]]:
        load[tmp[1]].append(tmp[0])

box=[]
answer=0
for i in range(1,n+1):
    box=[]
    if len(load[i])==0:
        answer+=1
    for j in range(len(load[i])):
        box.append(height[load[i][j]-1])
    if box!=[]:
        if max(box)<height[i-1]:
            answer+=1
print(answer)