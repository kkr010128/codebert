from collections import defaultdict
n = int(input())
dic = defaultdict(lambda: 0)
for _ in range(n):
    com = input().split(' ')
    if com[0]=='insert':
        dic[com[1]] = 1
    else:
        if com[1] in dic:
            print('yes')
        else:
            print('no')