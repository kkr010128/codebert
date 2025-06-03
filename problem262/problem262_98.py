n = int(input())
a = []

for i in range(n):
    temp = []
    temp_temp = []
    temp.append(int(input()))
    for j in range(temp[0]):
        temp_temp.append(list(map(int,input().split())))
    temp.append(temp_temp)
    a.append(temp)

ans = 0

for i in range(2**n):
    ans_t = 0
    id_list =list(bin(i))[2:]
    id_list = [int(x) for x in id_list]
    while len(id_list) != n:
        id_list.insert(0,0)
    for j in range(n):
        flag = 0
        if id_list[j] == 0:
            continue
        else:
            for k in range(a[j][0]):
                if id_list[a[j][1][k][0]-1] != a[j][1][k][1]:
                    flag = 1
                    break
        if flag == 1:
            ans_t = 0
            break
        else:
            ans_t += 1
    if ans_t > ans:
        ans = ans_t

print(ans)
