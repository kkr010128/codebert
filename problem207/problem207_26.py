A = []
for _ in range(3):
    a = [int(a) for a in input().split()]
    A.append(a)
N = int(input())
for _ in range(N):
    num = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j]==num:
                A[i][j] = -1

# Rows
for row in range(3):
    bingo_row = True
    for col in range(3):
        if A[row][col]!=-1:
            bingo_row = False
    if bingo_row:
        print('Yes')
        exit()
    
# Columns
for col in range(3):
    bingo_col = True
    for row in range(3):
        if A[row][col]!=-1:
            bingo_col = False
    if bingo_col:
        print('Yes')
        exit()

# Naname
bingo_naname = True
for i in range(3):
    col, row = i, i
    if A[row][col] != -1:
        bingo_naname = False
if bingo_naname:
    print('Yes')
    exit()
bingo_naname = True
for i in range(3):
    col, row = 2-i, i
    if A[row][col] != -1:
        bingo_naname = False
if bingo_naname:
    print('Yes')
    exit()

print('No')
