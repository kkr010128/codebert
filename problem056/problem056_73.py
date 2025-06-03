A = []
b = []

row, col = (int(x) for x in input().split())

for i in range(row):
    A.append([int(x) for x in input().split()])

for i in range(col):
    b.append(int(input()))

for i in range(row):
    print(sum(A[i][j]*b[j] for j in range(col)))