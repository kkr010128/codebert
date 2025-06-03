board, dp = [], []
bingo = False

for _ in range(3):
    board.append(list(map(int, input().split()))) 
    dp.append([0, 0, 0])

N = int(input())

for _ in range(N):
    num = int(input())

    for r in range(3):
        for c in range(3):
            if num == board[r][c]:
                dp[r][c] = 1

for i in range(3):
    if dp[i][0] == dp[i][1] == dp[i][2] == 1 or dp[0][i] == dp[1][i] == dp[2][i] == 1:
        bingo = True
        print("Yes")
        break

if not bingo:
    if dp[0][0] == dp[1][1] == dp[2][2] == 1 or dp[0][2] == dp[1][1] == dp[2][0] == 1:
        print("Yes")
    else:
        print("No")

