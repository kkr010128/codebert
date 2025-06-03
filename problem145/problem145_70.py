from collections import deque
N, M = map(int,input().split()) 
P = [list(map(int,input().split())) for i in range(M)]
A = [ [] for _ in range(N)]
#node_info = [{'node':d,'connect':[],'depth':-1,'dir':-1} for d in range(N)]

for path in P:
    A[path[1]-1].append(path[0]-1)
    A[path[0]-1].append(path[1]-1)
#print(A)

previous = [-1 for i in range(N)]
previous[0]=0

que = deque([0])

while len(que) != 0:
    v = que.popleft()
    for v_i in A[v]:
        if previous[v_i] != -1:
            continue
        else:
            que.append(v_i)
            previous[v_i] = v
for i in range(N):
    if previous[i] == -1:
        print('No')
        exit()
print('Yes')
for i in range(1,N):
    print(previous[i]+1)