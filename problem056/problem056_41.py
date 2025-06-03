matrix = []
vector = []
n, m = [int(x) for x in input().split()]

for i in range(n):
    matrix.append([int(x) for x in input().split()])
for i in range(m):
    vector.append(int(input()))

for i in range(n):
    sum = 0
    for j in range(m):
        sum += matrix[i][j] * vector[j]
    print(sum)