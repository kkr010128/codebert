r, c = map(int, input().split())
element = [list(map(int, input().split())) for i in range(r)]
for i in range(r):
    element[i].append(sum(element[i]))
for i in range(r):
    for j in range(c):
        print(element[i][j],end="")
        print(' ',end="")
    print(element[i][c])
for i in range(c):
    num = 0
    for j in range(r):
        num += element[j][i]
    print(num, end="")
    print(' ',end="")
b = 0
for i in range(r):
    b += element[i][c]
print(b)

