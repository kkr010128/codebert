n, m = [int(i) for i in input().split()]

matrix = []
for ni in range(n):
    matrix.append([int(a) for a in input().split()])

vector = []
for mi in range(m):
    vector.append(int(input()))

b = []
for ni in range(n):
    sum = 0
    for mi in range(m):
        sum += matrix[ni][mi] * vector[mi]

    print(sum)