from queue import deque

h,w = map(int,input().split())
li = [input() for _ in range(h)]

inf = 10**10
dx = [1,0]
dy = [0,1]
que = deque()

#そのマスにたどり着くまでに色が変わった最小の回数を保存するリスト
flip_count = [[inf for i in range(w)]for j in range(h)]

if li[0][0] == "#":
    flip_count[0][0] = 1
else:
    flip_count[0][0] = 0

que.append([0,0])

while que:
    k = que.popleft()
    x = k[0]
    y = k[1]
    for i,j in zip(dx,dy):
        nx = x + i
        ny = y + j
        if nx >= w or ny >= h:
            continue
        if flip_count[ny][nx] == inf:
            que.append([nx,ny])
        if li[ny][nx] != li[y][x]:
            flip_count[ny][nx] = min(flip_count[ny][nx],flip_count[y][x]+1)
        else:
            flip_count[ny][nx] = min(flip_count[ny][nx],flip_count[y][x])

if li[-1][-1] == "#":
    flip_count[-1][-1] += 1

print(flip_count[-1][-1]//2)