from collections import deque
n,m=map(int,input().split())
ab=[list(map(int, input().split())) for _ in range(m)]
l=[[] for i in range(n)]#各部屋とつながっている部屋
#print(l,ab)
for a,b in ab:
    l[a-1].append(b)
    l[b-1].append(a)
result=[-1]*n
q=deque([1])
#print(l,result)
while True:
    if len(q)==0:
        break
    x=q.popleft()
    for j in l[x-1]:
        if result[j-1]==-1:
            result[j-1]=x
            q.append(j)
    #print(q,result)

print("Yes")
[print(i) for i in result[1:]]