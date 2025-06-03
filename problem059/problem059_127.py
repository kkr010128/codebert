r,c = map(int,raw_input().split())
matrix = []
for i in range(r):
    matrix.append(map(int,raw_input().split()))

a = [0 for j in range(c)]

matrix.append(a)

for i in range(r):
    sum = 0
    for j in range(c):
        sum += matrix[i][j]
    matrix[i].append(sum)

for j in range(c):
    sum = 0
    for i in range(r):
        sum += matrix[i][j]
    matrix[r][j] = sum

sum = 0
for j in range(c):  
    sum += matrix[r][j]
matrix[r].append(sum)

for i in range(r):
    for j in range(c):
        print matrix[i][j],
    print matrix[i][c]

for j in range(c + 1):
    print matrix[r][j],