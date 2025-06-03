n = int(input())

d = set()
for i in range(n):
    com = input().split()
    if com[0] == 'insert':
        d.add(com[1])
    else:
        print('yes' if com[1] in d else 'no')