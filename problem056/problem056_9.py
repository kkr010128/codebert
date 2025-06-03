row, col = map(int,input().split())

mat = [[0 for i2 in range(col)] for i1 in range(row)]
for i in range(row):
    mat[i] = list(map(float,input().split()))
vec = [0 for i in range(col)]
for i in range(col):
       vec[i] = float(input())

result = [0 for i in range(row)]
for i in range(row):
    for j in range(col):
        result[i] += mat[i][j]*vec[j]

for i in range(len(result)):
    print(int(result[i]))