import queue

h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
# print(maze)

def bfs(dist, i, j):
    q = queue.Queue()
    q.put((i, j, 0))
    while not q.empty():
        i, j, c = q.get()
        # print(i, j, c, dist)
        if i != 0 and dist[i-1][j] == 0:
            dist[i-1][j] = c+1
            q.put((i-1, j, c+1))
        if j != 0 and dist[i][j-1] == 0:
            dist[i][j-1] = c+1
            q.put((i, j-1, c+1))
        if i != h-1 and dist[i+1][j] == 0:
            dist[i+1][j] = c+1
            q.put((i+1, j, c+1))
        if j != w-1 and dist[i][j+1] == 0:
            dist[i][j+1] = c+1
            q.put((i, j+1, c+1))
    return dist, c

ans = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            dist = [[(maze[y][x] == '#')*-1 for x in range(w)] for y in range(h)]
            dist[i][j] = -10
            dist, c = bfs(dist, i, j)
            tmp_ans = c
            if tmp_ans > ans:
                ans = tmp_ans

print(ans)
