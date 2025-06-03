# coding: utf-8
n, m = map(int, input().split())
matrixA = []
vectorB = []

for i in range(n):
    matrixA.append(list(map(int, input().split())))

for i in range(m):
    vectorB.append(int(input()))


for i in range(n):
    num = 0
    for j in range(m):
        num += matrixA[i][j] * vectorB[j]
    print(num)

