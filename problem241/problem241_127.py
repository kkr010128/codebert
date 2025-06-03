def resolve():
    H, W = list(map(int, input().split()))
    S = [list(input()) for _ in range(H)]
    import collections
    maxdist = 0

    for startx in range(H):
        for starty in range(W):
            if S[startx][starty] == "#":
                continue
            visited = [[-1 for _ in range(W)] for __ in range(H)]
            visited[startx][starty] = 0
            q = collections.deque([(startx, starty)])
            while q:
                x, y = q.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] != "#" and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.appendleft((nx, ny))
            maxdist = max(maxdist,max(sum(visited, [])))
    print(maxdist)
    

if '__main__' == __name__:
    resolve()
