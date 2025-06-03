from collections import deque
h,w=map(int,input().split())
l=list()
l.append('#'*(w+2))#壁
for i in range(h):
    l.append('#'+input()+'#')
l.append('#'*(w+2))#壁
p=0
for i in range(1,h+1):
    for j in range(1,w+1):
        if l[i][j]=='#':
            continue
        s=[[-1 for a in b] for b in l]
        q=deque([[i,j]])
        s[i][j]=0
        while len(q)>0:
            a,b=q.popleft()
            for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                if l[a+x][b+y]=='#' or s[a+x][b+y]>-1:
                    continue
                q.append([a+x,b+y])
                s[a+x][b+y]=s[a][b]+1
        r=0
        for x in s:
            for y in x:
                r=max(y,r)
        p=max(r,p)
print(p)