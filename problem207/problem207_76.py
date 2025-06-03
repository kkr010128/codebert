a = [list(map(int,input().split())) for i in range(3)]
n = int(input())
for i in range(n):
    b = int(input())
    for x in range(3):
        for y in range(3):
            if a[x][y] == b:
                a[x][y] = 'o'
for x in range(3):
    if a[x][0] == a[x][1] == a[x][2] == 'o':
        print('Yes')
        exit(0)
for y in range(3):
    if a[0][y] == a[1][y] == a[2][y] == 'o':
        print('Yes')
        exit(0)
if a[0][0] == a[1][1] == a[2][2] == 'o':
    print('Yes')
elif a[0][2] == a[1][1] == a[2][0] == 'o':
    print('Yes')
else:
    print('No')