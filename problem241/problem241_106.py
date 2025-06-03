from collections import deque


# 隣り合ったマスへ移動するためのテーブル
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

H, W = map(int, input().split())
maze = [input() for _ in range(H)]

# 全ての"."の地点からBFSしてスタートからの各地点への移動回数(深さ)を調べ、最大のものを出力する
def solve():
    ans = 0
    for i in range(H):
        for j in range(W):
            # スタートが壁の場合
            if maze[i][j] == "#":
                continue
        
            # BFSの初期化、初期条件
            dist = [[-1] * W for _ in range(H)]
            dist[i][j] = 0
            que = deque()
            que.append([i, j])

            # BFSループ
            while que:
                y, x = que.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    # 迷路から外れる場合
                    if nx >= W or nx < 0 or ny >= H or ny < 0:
                        continue
                    # 既に探索済みの場合
                    if dist[ny][nx] != -1:
                        continue
                    # 隣が壁の場合
                    if maze[ny][nx] == "#":
                        continue
                    dist[ny][nx] = dist[y][x] + 1
                    que.append([ny, nx])

            ans = max(ans, max(max(steps) for steps in dist))
    print(ans)


if __name__ == "__main__":
    solve()
