s_list = input()
t_list = input()

n = len(s_list)

if s_list == t_list[:-1]:
    print('Yes')
else:
    print('No')