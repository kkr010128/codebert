import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W = map(int, readline().split())
    S = [[0] * W for _ in range(H)]
    for i in range(H):
        S[i] = readline().strip()

    dxdy4 = ((-1, 0), (0, -1), (0, 1), (1, 0))

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            dist = [[-1] * W for _ in range(H)]
            dist[i][j] = 0
            queue = deque([(i, j)])
            res = 0
            while queue:
                x, y = queue.popleft()
                for dx, dy in dxdy4:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        if res < dist[nx][ny]:
                            res = dist[nx][ny]
                        queue.append((nx, ny))
            if ans < res:
                ans = res

    print(ans)
    return


if __name__ == '__main__':
    main()
