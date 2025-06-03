from collections import deque
h, w = map(int, input().split())
chiz = [[] for _ in range(w)]
for _ in range(h):
    tmp_list = input()
    for i in range(w):
        chiz[i].append(tmp_list[i])
def bfs(i,j):
    ds = [[-1]*h for _ in range(w)]
    dq = deque([(i,j)])
    ds[i][j] = 0
    res = -1
    while dq:
        i,j = dq.popleft()
        for move in [(1,0),(-1,0),(0,-1),(0,1)]:
            if i+move[0] >= 0 and i+move[0] < w and j+move[1] >= 0 and j+move[1] < h:
                if chiz[i+move[0]][j+move[1]]=='.' and ds[i+move[0]][j+move[1]] == -1:
                    ds[i + move[0]][j + move[1]] = ds[i][j] + 1
                    res = max(res,ds[i + move[0]][j + move[1]])
                    dq.append((i + move[0],j + move[1]))
    return res
res = -1
for j in range(h):
    for i in range(w):
        if chiz[i][j]=='.':
            res = max(res, bfs(i,j))
print(res)