# coding: utf-8
d = {}
N = int(input())

for _ in range(N):
    ope, s = map(str, input().split())
    if ope == 'insert':
        d[s] = 0
    elif ope == 'find':
        if s in d.keys():
            print('yes')
        else:
            print('no')

