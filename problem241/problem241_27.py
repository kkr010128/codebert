from collections import deque
import numpy as np

# (sx, sy) から (gx, gy) への最短距離を求める
# 辿り着けないと INF
def bfs(sx, sy):
    # すべての点を INF で初期化
    d = [[float("-inf")] * m for i in range(n)]

    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # スタート地点をキューに入れ、その点の距離を0にする
    que = deque([])
    que.append((sx, sy))
    d[sx][sy] = 0

    # キューが空になるまでループ
    while que:
        # キューの先頭を取り出す
        p = que.popleft()
        # 取り出してきた状態がゴールなら探索をやめる
        #if p[0] == gx and p[1] == gy:
        #    break
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を (nx, ny) とする
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            # d[nx][ny] != INF なら訪れたことがある
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != "#" and d[nx][ny] == float("-inf"):
                # 移動できるならキューに入れ、その点の距離を p からの距離 +1 で確定する
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    a = np.max(d) 
    return a

n, m = map(int, input().split())
maze = [list(input()) for i in range(n)]
ans = 1

for x in range(n):
    for y in range(m):
        sx = x
        sy = y
        if maze[sx][sy] == "#":
            continue
        A = bfs(sx, sy)
        ans = max(A, ans)
print(int(ans))