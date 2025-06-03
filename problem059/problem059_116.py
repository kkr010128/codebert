num = [[0 for i in range(101)] for j in range(101)]
r, c = map(int, input().split())
for i in range(r):
    num[i][:c] = list(map(int, input().split()))
    for j in range(c):
        num[i][c] += num[i][j]
for j in range(c+1):
    for i in range(r):
        num[r][j] += num[i][j]
for i in range(r+1):
    for j in range(c):
        print(num[i][j], end=' ')
    print(num[i][c])