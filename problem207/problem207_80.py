matrix = []
for i in range(3):
    line = []
    line = input().split(" ")
    matrix.append(line)

n = int(input())
chosen = 0

for i in range(n):
    b = input()
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == b:
                chosen += 1
                matrix[i][j] = 0
bingo = False
for i in range(3):
    if(matrix[i][0] == 0 and matrix[i][1] == 0 and matrix[i][2] == 0):
        bingo = True
        break
    elif(matrix[0][i] == 0 and matrix[1][i] == 0 and matrix[2][i] == 0):
        bingo = True
        break

if(matrix[1][1] == 0 and matrix[0][0] == 0 and matrix[2][2] == 0):
    bingo = True
if(matrix[1][1] == 0 and matrix[2][0] == 0 and matrix[0][2] == 0):
    bingo = True
if bingo:
    print("Yes")
else:
    print("No")
