from collections import deque
n,x,y=map(int,input().split())
l=[[1]]
for i in range(1,n-1):
    l.append([i-1,i+1])
l.append([n-2])
x,y=x-1,y-1
l[x].append(y)
l[y].append(x)
#print(l)
p=[0 for i in range(n)]
for j in range(n):
    s=[-1 for i in range(n)]
    s[j]=0
    q=deque([j])
    while len(q)>0:
        a=q.popleft()
        for i in l[a]:
            if s[i]==-1:
                s[i]=s[a]+1
                q.append(i)
    for i in s:
        if i!=0:
            p[i]+=1
print(*map(lambda x:x//2,p[1:]),sep='\n')