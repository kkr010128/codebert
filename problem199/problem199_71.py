a = input()
hi_cnt = a.count('hi')
if hi_cnt > 0:
    if hi_cnt * 2 == len(a):
        print('Yes')
    else:
        print('No')
else:
    print('No')