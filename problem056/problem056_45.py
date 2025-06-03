size = [int(i) for i in input().split()]
matrix = [[0 for i in range(size[1])] for j in range(size[0])]
vector = [0 for i in range(size[1])]
for gyou in range(size[0]):
    x = [int(i) for i in input().split()]
    matrix[gyou] = x
for retsu in range(size[1]):
    x = int(input())
    vector[retsu] = x

for gyou in range(size[0]):
    print(sum(map(lambda val1, val2: val1 * val2, matrix[gyou], vector)))

