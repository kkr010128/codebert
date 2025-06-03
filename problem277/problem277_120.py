H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]
ans = [[0]*W for _ in range(H)]
empty_index = [False]*H
first_flg = False
cnt = 0
for i in range(H):
    if '#' not in grid[i]:
        empty_index[i] = True
for i in range(H):
    if not empty_index[i] and not first_flg:
        first_flg = True
        first_index = i
    if not first_flg:
        continue
    if empty_index[i]:
        for k in range(W):
            ans[i][k] = ans[i-1][k]
    else:
        cnt += 1
        flg = False
        for k in range(W):
            if grid[i][k] == '#':
                if not flg:
                    flg = True
                else:
                    cnt += 1
            ans[i][k] = cnt
for i in range(H):
    if not empty_index[i]:
        break
    for k in range(W):
        ans[i][k] = ans[first_index][k]
for i in ans:
    print(*i)