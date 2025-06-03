from collections import deque

n, m = map(int,input().split())
turo = [[] for i in range(n+1)]
sirusi = [-1 for i in range(n+1)]

for i in range(m):
    tmp = list(map(int,input().split()))
    turo[tmp[0]].append(tmp[1])
    turo[tmp[1]].append(tmp[0])

sirusi[1] = 0

q = deque()
q.append(1)

while len(q) != 0:
    x = q.popleft()
    for i in turo[x]:
        if sirusi[i] == -1:
            sirusi[i] = x
            q.append(i)

print('Yes')
for i in range(n+1):
    if i != 0 and i != 1:
        print(sirusi[i])
