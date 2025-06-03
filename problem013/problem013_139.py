cnt = 0
for i in range(int(input())):
    c_num = int(input())
    if cnt == 0:
        r_min = c_num
    elif cnt == 1:
        p_max = c_num - r_min
        if c_num < r_min:
            r_min = c_num
    else:
        if p_max < c_num - r_min:
            p_max = c_num - r_min
        if c_num < r_min:
            r_min = c_num
    cnt += 1
print(p_max)

