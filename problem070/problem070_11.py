n,m=map(int, input().split())

arr=[[] for i in range(n+1)]

gro=[0]*(n+1)

for i in range(m):
    a,b=map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

from collections import deque
deque=deque()

gro_no=0

for i in range(1,n+1):
    if gro[i]==0:
        gro_no+=1
        gro[i]=gro_no
        deque.append(i)

    while deque:
        j=deque.popleft()
        for k in arr[j]:
            if gro[k]==0:
                gro[k]=gro_no
                deque.append(k)

print(gro_no-1)