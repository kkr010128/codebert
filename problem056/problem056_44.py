n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]

for obj in matrix:
    print(sum(obj[i] * b[i] for i in range(m)))