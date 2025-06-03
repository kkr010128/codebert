d = set()
n = int(input())
for i in range(n):
    raw=input().split()
    if raw[0] == 'insert':
        d.add(raw[1])
    else:
        if raw[1] in d:
            print('yes')
        else:
            print('no')

