card = []
check = [[0, 0, 0] for i in range(3)]
for i in range(3):
    card.append(list(map(int, input().split())))

n = int(input())
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if b == card[j][k]:
                check[j][k] = 1

flag = 0

for i in range(3):
    if check[i][0] == check[i][1] == check[i][2] == 1:
        flag = 1
        break
    elif check[0][i] == check[1][i] == check[2][i] == 1:
        flag = 1
        break
    elif check[0][0] == check[1][1] == check[2][2] == 1:
        flag = 1
        break
    elif check[0][2] == check[1][1] == check[2][0] == 1:
        flag = 1
        break

if flag:
    print('Yes')
else:
    print('No')