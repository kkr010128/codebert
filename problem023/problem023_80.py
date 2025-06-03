a = int(input())

d = {}
for i in range(a):
    o,v = input().split()
    if o == 'insert':
        d[v] = v
    elif o == 'find':
        if v in d:
            print('yes')
        else:
            print('no')

