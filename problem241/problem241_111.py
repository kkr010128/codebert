from collections import deque
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def bfs(field, sx, sy, seen):
    queue = deque([(sx, sy)])
    seen[sx][sy] += 1
    
    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            
            if seen[nx][ny] == -1 and field[nx][ny] != "#":
                seen[nx][ny] = seen[x][y] + 1
                queue.append((nx, ny))

    return seen[x][y]


def main():
    H,W = map(int, readline().split())
    c = ["#" * (W + 2)]
    for _ in range(H):
        c.append("#" + readline().strip() + "#")
    c.append("#" * (W + 2))

    ans = 0
    for sx in range(1,H+1):
        for sy in range(1,W+1):
            if c[sx][sy] == ".":
                seen = [[-1] * (W + 2) for i in range(H+2)]
                dist = bfs(c, sx, sy, seen)
                ans = max(ans, dist)

    print(ans)


if __name__ == "__main__":
    main()
