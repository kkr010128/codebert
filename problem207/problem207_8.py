board=[0,0,0,0,0,0,0,0,0]
board[0],board[1],board[2] = map(int,input().split())
board[3],board[4],board[5] = map(int,input().split())
board[6],board[7],board[8] = map(int,input().split())
for _ in range(int(input())):
    x = int(input())
    if x in board:
        board[board.index(x)] = "X"
found = "No"
if board[0] == "X":
    if board[1] == "X" and board[2] == "X":
        found = "Yes"
    elif board[4] == "X" and board[8] == "X":
        found = "Yes"
    elif board[3] == "X" and board[6] == "X":
        found = "Yes"
if board[8] == "X":
    if board[5] == "X" and board[2] == "X":
        found = "Yes"
    elif board[7] == "X" and board[6] == "X":
        found = "Yes"
if board[4] == "X":
    if board[1] == "X" and board[7] == "X":
        found = "Yes"
    elif board[3] == "X" and board[5] == "X":
        found = "Yes"
    elif board[2] == "X" and board[6] == "X":
        found = "Yes"
print(found)