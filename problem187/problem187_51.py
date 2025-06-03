n,x,y=map(int,input().split())

ans=[0]*n

tree=[[] for _ in range(n)]

for i in range(1,n):
    tree[i-1].append(i)
    tree[i].append(i-1)

tree[x-1].append(y-1)
tree[y-1].append(x-1)

from collections import deque

ans=[0]*n
for i in range(n):
    checked=[-1]*n
    stack=deque([i])
    checked[i]=0
    while len(stack)>0:
        tmp=stack.popleft()
        for item in tree[tmp]:
            if checked[item]==-1:
                checked[item]=checked[tmp]+1
                stack.append(item)
    for item in checked:
        ans[item]+=1

for item in ans[1:]:
    print(item//2)



