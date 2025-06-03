n = int(input())
str_list = list(map(list,input().split(' ')))

ans_list = []
for i in range(n):
    ans_list.append(str_list[0][i])
    ans_list.append(str_list[1][i])
ans_str = ''.join(ans_list)
print(ans_str)
