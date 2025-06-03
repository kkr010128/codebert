N = int(input())

if N > 81:
    print('No')

ans_list = []
if N <= 81:
    for i in range(1,10):
        for j in range(1,10):
            ans_list.append(i * j) 
    if N in ans_list:
        print('Yes')
    if N not in ans_list:
        print('No')