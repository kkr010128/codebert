# coding:utf-8

# ??\???
n,m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append([0] * m)

for i in range(n):
    col = input().split()
    for j in range(m):
        matrix[i][j] = int(col[j])

vector = [0] * m
for j in range(m):
    vector[j] = int(input())

for i in range(n):
    row_sum = 0
    for j in range(m):
        row_sum += matrix[i][j] * vector[j]
    print(row_sum)