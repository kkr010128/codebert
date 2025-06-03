import sys
from collections import deque

def main():
    h, w = map(int, input().split())
    maze = [input() for i in range(h)]
    # 行ったかどうかのフラグ
    visited = [[-1]*w for j in range(h)]
    start_yx = []
    for i in range(h):
        for j in range(w):
            if maze[i][j] == '.':
                sy = i
                sx = j
                start_yx .append([sy, sx])

    # 移動パターン
    mv = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ans = 0
    for sy, sx in start_yx :
        visited = [[-1]*w for j in range(h)]
        q = deque([[sy, sx]])
        visited[sy][sx] = 0 
        while q:
            y, x = q.popleft()
            ans = max(ans, visited[y][x])
            for i, j in mv:
                if (0 <= y + i < h) and (0 <= x + j < w):  
                    ny = y+i
                    nx = x+j
                    if visited[ny][nx] != -1:
                        continue
                    if maze[ny][nx] == '.':
                        visited[ny][nx] = visited[y][x] + 1 
                        q.append([ny, nx])
                else:
                    continue
    print(ans)

if __name__ == '__main__':
    main()


