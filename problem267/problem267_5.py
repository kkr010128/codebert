n = int(input())
num_list = list(map(int,input()))

cnt = 0

for i in range(10):
    if i not in num_list:
        continue
    else:
        first_pwd = num_list.index(i)
        new_num_list = num_list[first_pwd + 1:]
        for j in range(10):
            if j not in new_num_list:
                continue
            else:
                second_pwd = new_num_list.index(j)
                new_new_num_list = new_num_list[second_pwd+1:]
                for k in range(10):
                    if k not in new_new_num_list:
                        continue
                    else:
                        cnt += 1

print(cnt)