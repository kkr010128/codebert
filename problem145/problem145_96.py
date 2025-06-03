n,m=map(int,input().split())
graph=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

sign=[-1]*n
sign[0]=0
work=[]
work_next=graph[0]
for x in work_next:
    sign[x]=0


while work_next:
    work=work_next[:]
    work_next=[]
    for x in work:
        for y in graph[x]:
            if sign[y]>=0 : continue
            if y in work_next : continue
            sign[y]=x
            work_next.append(y)

if -1 in sign : print("No");exit()
print("Yes")
for i in range(1,n):
    print(sign[i]+1)