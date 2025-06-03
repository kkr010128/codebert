a =[]

for i in range(3):
    a .append(list(map(int, input().split())))


n = int(input())
b =[]

for i in range(n):
    b.append(int(input()))



flag = 0
cnt = 0
# yoko
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            cnt += 1
    else:
        if cnt == 3:
            print("Yes")
            flag += 1
            exit()
        else:
            cnt = 0

# tate
if flag == 0:
    for i in range(3):
        for j in range(3):
            if a[j][i] in b:
                cnt += 1

        else:
            if cnt == 3:
                print("Yes")
                flag += 1
                exit()
            else:
                cnt = 0


# ななめ1
if flag == 0:
    for i in range(3):
        if a[i][i] in b:
             cnt += 1
    else:
        if cnt == 3:
            print("Yes")
            flag += 1
            exit()
        else:
            cnt = 0

# ななめ2
if flag == 0:
    if a[2][0] in b:
        if a[1][1] in b:
            if a[0][2] in b:
                print("Yes")
                flag += 1


if flag == 0:
    print("No")
