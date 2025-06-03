r, c= map(int, input().split())
list = [list(map(int,input().split())) for i in range(r)]
for i in range(r):
    list[i].append(sum(list[i]))
for i in range(r):
    for j in range(c):
        print(list[i][j], end = ' ')
    print(list[i][c])
for i in range(c):
    a = 0
    for j in range(r):
        a += list[j][i]
    print(a, end = ' ')
a = 0
for j in range(r):
    a += list[j][c]
print(a)

