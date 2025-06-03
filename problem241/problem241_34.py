from collections import deque
import itertools

h, w = map(int, input().split())
g = [input() for _ in range(h)]


# x,yはスタートの座標
def bfs(x, y):
    # 最初は全て未訪問なので-1で初期化
    d = [[-1] * w for _ in range(h)]
    # スタート地点への距離は0
    d[x][y] = 0
    q = deque([(x, y)])
    while q:
        tx, ty = q.popleft()
        # 右、上、左、下
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = tx + dx, ty + dy
            # グリッドの範囲(縦方向, 横方向)内、通路(壁ではない)、未訪問(== -1)の場合
            if 0 <= nx < h and 0 <= ny < w and g[nx][ny] == '.' and d[nx][ny] < 0:
                d[nx][ny] = d[tx][ty] + 1
                q.append((nx, ny))
    # 最終的なdを平坦化して最大値を返す
    return max(list(itertools.chain.from_iterable(d)))


# 全てのマスについて
max_count = 0
for x in range(h):
    for y in range(w):
        # スタートが通路であるかチェックする必要がある
        if g[x][y] == ".":
            max_count = max(max_count, bfs(x, y))

print(max_count)
