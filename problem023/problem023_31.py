import sys
n = int(input())
dic =set()

t = sys.stdin.readlines()

for i in t:
    i,op = i.split()
    if i == 'insert':
        dic.add(op)    
    else:
        if op in dic:
            print('yes')
        else:
            print('no')