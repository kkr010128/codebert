N,M = map(int,input().split())
A = [0]*M
B = [0]*M
for i in range(M):
    A[i],B[i] = map(int,input().split())

from collections import deque
links = [[] for _ in range(N+1)]
for i in range(M):
    links[A[i]].append(B[i])
    links[B[i]].append(A[i])

result = [-1]*(N+1)
q  = deque([1])
while q:
    i = q.popleft()
    for j in links[i]:
        if result[j] == -1:
            result[j] = i
            q.append(j)
        
        
print('Yes')
print('\n'.join(str(i) for i in result[2:]))