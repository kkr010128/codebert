import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def main():
    H,W = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    dp = [[float('inf') for _ in range(W)] for _ in range(H)]

    def bfs(x,y):
        que = deque()
        que.append((x,y))
        if S[y][x] == '.':
            dp[y][x] = 0
        else:
            dp[y][x] = 1
        while que.__len__():
            x,y = que.popleft()
            for dx,dy in ((1,0),(0,1)):
                sx = x + dx
                sy = y + dy
                if sx == W or sy == H:
                    continue
                if S[y][x] == '.' and S[sy][sx] == '#':
                    tmp = 1
                else:
                    tmp = 0
                dp[sy][sx] = min(dp[y][x]+tmp,dp[sy][sx])
                if (sx,sy) not in que:
                    que.append((sx,sy))
    bfs(0,0)
    print(dp[H-1][W-1])
if __name__ == "__main__":
    main()