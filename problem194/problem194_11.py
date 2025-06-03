h,w = list(map(int, input().split()))
board = []
dp = []
INF=10**18
for _ in range(h):
    board.append(input())
    dp.append([INF]*w)

dxy=[(0,1), (0,-1), (1,0), (-1,0)]

dp[0][0]=1 if board[0][0] == '#' else 0
for y in range(h):
    for x in range(w):
        dp_list=[dp[y][x]]
        if x>0:
            dp_left = dp[y][x-1]
            if board[y][x-1] != board[y][x] and board[y][x] == '#':
                dp_left += 1
            dp_list.append(dp_left)
        if y>0:
            dp_up=dp[y-1][x]
            if board[y-1][x] != board[y][x] and board[y][x] == '#':
                dp_up += 1
            dp_list.append(dp_up)
        dp[y][x]=min(dp_list)

print(dp[h-1][w-1])