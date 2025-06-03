import sys

n = int(input())
dic = set()
input_ = [x.split() for x in sys.stdin.readlines()]

for c, s in input_:
    if c == 'insert':
        dic.add(s)
    else:
        if s in dic:
            print('yes')
        else:
            print('no')