def input_li():
    return list(map(int, input().split()))

def input_int():
    return int(input())

H, W = input_li()
board = [input() for _ in range(H)]
# dp[x][y] ... マス(x, y)時点で実行した操作の最小回数
dp = [[10 ** 9] * W for _ in range(H)]
dp[0][0] = 1 if board[0][0] == '#' else 0
for h in range(H):
    for w in range(W):
        is_now_black = board[h][w] == '#'
        if h == 0 and w != 0:
            dp[h][w] = dp[h][w - 1] + (1 if is_now_black and board[h][w - 1] == '.' else 0)
        elif h != 0 and w == 0:
            dp[h][w] = dp[h - 1][w] + (1 if is_now_black and board[h - 1][w] == '.' else 0)
        elif h != 0 and w != 0:
            from_w = dp[h][w - 1] + (1 if is_now_black and board[h][w - 1] == '.' else 0)
            from_h = dp[h - 1][w] + (1 if is_now_black and board[h - 1][w] == '.' else 0)
            dp[h][w] = min(from_h, from_w)
print(dp[-1][-1])
