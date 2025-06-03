from collections import deque
h,w = map(int, input().split())
hw = [input() for _ in range(h)]

def bfs(s):
    que = deque([s])
    m = [[-1]*w for _ in range(h)]
    sh, sw = s
    m[sh][sw] = 0
    ret = 0
    while que:
        now_h, now_w = que.popleft()
        for dh, dw in [(1,0), (-1,0), (0,-1), (0,1)]:
            nh = now_h + dh
            nw = now_w + dw
            if not (0<=nh<h and 0<=nw<w) or m[nh][nw] != -1 or hw[nh][nw] == '#':
                continue
            m[nh][nw] = m[now_h][now_w] + 1
            que.append((nh,nw))
            ret = max(ret, m[now_h][now_w] + 1)
    return ret

ans = 0
for y in range(h):
    for x in range(w):
        if hw[y][x] == '#':
            continue
        s = (y, x)
        ans = max(bfs(s), ans)

print(ans)