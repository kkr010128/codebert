r,c = map(int,input().split())
matrix = [list(map(int,input().split())) for i in range(r)]
for i in range(r):
    matrix[i].append(sum(matrix[i]))

row = []

for i in range (c+1):
    row_sum = 0
    for j in range(r):
        row_sum += matrix[j][i]
    row.append(row_sum)

matrix.append(row)
for i in range(r+1):
    for j in range(c+1):
        print(matrix[i][j],end="")
        if j != c:
            print(" ",end="")
        if j == c :
            print("")