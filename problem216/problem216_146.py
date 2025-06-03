list = list(map(int, input().split()))
list_num=set(list)
if len(list_num)==2:
    print('Yes')
else:
    print('No')