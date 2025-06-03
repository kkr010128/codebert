N, u, v = map(int, input().split())
u, v = u-1, v-1

ABs = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N-1)]

#%%
roots = [[] for _ in range(N)]

for AB in ABs:
    roots[AB[0]].append(AB[1])
    roots[AB[1]].append(AB[0])

#BFS
def BFS(roots, start):
    from collections import deque
    seen = [-1 for _ in range(N)]
    seen[start] = 0
    todo = deque([start])
    while len(todo) > 0:
        checking = todo.pop()
        for root in roots[checking]:
            if seen[root] == -1:
                seen[root] = seen[checking] +1
                todo.append(root)
    return seen

from_u = BFS(roots, u)
from_v = BFS(roots, v)

from collections import deque
todo = deque([u])
max_distance = from_v[u]
position = u
seen = [False for _ in range(N)]
seen[u] = True
while len(todo) > 0:
    checking = todo.pop()
    for root in roots[checking]:
        if from_u[root] < from_v[root] and seen[root] == False:
            seen[root] = True
            todo.append(root)

            if max_distance < from_v[root]:
                max_distance = from_v[root]
                position = root
            
print(max_distance-1)