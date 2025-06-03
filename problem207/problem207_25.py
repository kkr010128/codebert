masu = [list(map(int,input().split())) for _ in range(3)]
n = int(input())
li = [int(input()) for _ in range(n)]
check = [[0]*3 for _ in range(3)]


for num in li:
    for i in range(3):
        for j in range(3):
            if masu[i][j] == num:
                check[i][j] = 1

for row in check:
    if all(row) == 1:
        print('Yes')
        exit()
for t in range(3):
    count = 0
    for row in check:
        if row[t] == 1:
            count += 1
    if count == 3:
        print('Yes')
        exit()
if check[0][0] + check[1][1] + check[2][2] == 3:
    print('Yes')
    exit()
if check[0][2] + check[1][1] + check[0][2] == 3:
    print('Yes')
    exit()
    
print('No')