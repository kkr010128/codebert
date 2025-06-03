# coding=utf-8

n = int(input())
dic = set()

for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        dic.add(cmd[1])
    else:
        if cmd[1] in dic:
            print('yes')
        else:
            print('no')