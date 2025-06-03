import sys

num = int(input())
dic = set()

for i in range(num):
    order = sys.stdin.readline().split()

    if order[0] == 'insert':
        dic.add(order[1])
    else:
        if order[1] in dic:
            print('yes')
        else:
            print('no')