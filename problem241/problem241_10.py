from collections import deque

H, W = map(int, input().split())
L = [str(input()) for _ in range(H)]
ans = 0
for h in range(H):
    for w in range(W):
        if L[h][w] == '#':
            continue
        else:
            flag = [[-1] * W for _ in range(H)]
            depth = [[0] * W for _ in range(H)]
            flag[h][w] = 0
            q = deque([(h, w)])
            while q:
                i, j = q.popleft()
                d = depth[i][j]
                if i != H - 1:
                    if L[i+1][j] == '.' and flag[i+1][j] < 0:
                        flag[i+1][j] = 0
                        depth[i+1][j] = d + 1
                        q.append((i+1, j))
                if i != 0:
                    if L[i-1][j] == '.' and flag[i-1][j] < 0:
                        flag[i-1][j] = 0
                        depth[i-1][j] = d + 1
                        q.append((i-1, j))
                if j != W - 1:
                    if L[i][j+1] == '.' and flag[i][j+1] < 0:
                        flag[i][j+1] = 0
                        depth[i][j+1] = d + 1
                        q.append((i, j+1))
                if j != 0:
                    if L[i][j-1] == '.' and flag[i][j-1] < 0:
                        flag[i][j-1] = 0
                        depth[i][j-1] = d + 1
                        q.append((i, j-1))
                ans = max(ans, d)
print(ans)
