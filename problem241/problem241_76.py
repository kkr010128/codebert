from collections import deque
import copy

h,w = map(int,input().split())
l = [['#']*(w+2)]
for i in range(h):
    l.append(['#']+list(input())+['#'])
l.append(['#']*(w+2))

ans = 0
directions = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(1,h+1):
    for j in range(1,w+1):
        visited = copy.deepcopy(l)
        if visited[i][j]=='.':
            visited[i][j] = 0
            que = deque([(i,j)])
            while que:
                v = que.popleft()
                for dir in directions:
                    nv = (v[0]+dir[0],v[1]+dir[1])
                    if visited[nv[0]][nv[1]] == '.':
                        times = visited[v[0]][v[1]]+1
                        visited[nv[0]][nv[1]] = times
                        que.append(nv)
                        ans = max(times,ans)
            # print((i,j),ans)

print(ans)