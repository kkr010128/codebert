n,m = map(int, input().split())
matrix = []
vector = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)
for j in range(m):
    vector.append(int(input()))
for k in range(n):
    entry = 0
    for l in range(m):
        entry += (matrix[k][l] * vector[l])
    print(entry)
