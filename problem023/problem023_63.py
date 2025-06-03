import sys
input()
rl = sys.stdin.readlines()
d = {}

for i in rl:
    c, s = i.split()
    #if i[0] == 'i':
    if c[0] == 'i':
        #d[i[7:]] = 0
        d[s] = 0
    else:
        #if i[5:] in d:
        if s in d:
            print('yes')
        else:
            print('no')