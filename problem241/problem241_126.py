H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

import queue, itertools

dxy = ((1,0), (-1,0), (0,1), (0,-1))
ans = 0
for s in itertools.product(range(H), range(W)):
    if S[s[0]][s[1]] == '#': continue
    
    q = queue.Queue()
    dist = [[-1]*W for _ in range(H)]     

    q.put(s)
    dist[s[0]][s[1]] = 0
    while not q.empty():
        y, x = q.get()         
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>=W or ny>=H or S[ny][nx] == '#' or dist[ny][nx] >= 0: 
                continue
            dist[ny][nx] = dist[y][x] + 1
            q.put((ny, nx))
    
    ans = max(ans, max(map(max, dist)))

print(ans)