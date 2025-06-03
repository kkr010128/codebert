N = int(input())
matrix = [[0,0,0,0,0,0,0,0,0,0] for _ in range(10)]
for i in range(1,N+1):
    first = int(str(i)[0])
    last = int(str(i)[-1])
    matrix[first][last] += 1
ans = 0
for i in range(10):
    for l in range(10):
        ans += matrix[i][l]*matrix[l][i]
print(ans)