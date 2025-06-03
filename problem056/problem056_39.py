rows, cols = [int(x) for x in input().split()]
matrix = []
vector = []
for i in range(rows):
    matrix.append([int(x) for x in input().split()])
for i in range(cols):
    vector.append(int(input()))

for row in matrix:
    result = 0
    for x, y in zip(row, vector):
        result += x*y
    print(result)