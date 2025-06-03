data = list(map(int, list(input().split())))
row = data[0]
column = data[1]
matrix = [[0 for i in range(column)] for j in range(row)]
vector = [[0] for k in range(column)]
vector_multi = [[0] for l in range(row)]

for i in range(row):
    data_row = list(map(int, list(input().split())))
    for j in range(column):
        matrix[i][j] = data_row[j]

for i in range(column):
    vector[i] = int(input())

for i in range(row): 
    element = 0
    for j in range(column):
        element += matrix[i][j] * vector[j]
    vector_multi[i][0] = element

for i in vector_multi:
    print(i[0])

