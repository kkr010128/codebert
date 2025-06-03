import sys

n = int(input())
dic = {}
input_ = [x.split() for x in sys.stdin.readlines()]

for c, s in input_:
    if c == 'insert':
        dic[s] = 0
    else:
        if s in dic:
            print('yes')
        else:
            print('no')