n = int(input())
s = set()
for i in range(n):
    a,b = input().strip().split()
    if a == 'insert':
        s.add(b)
    if a == 'find':
        if b in s:
            print('yes')
        else:
            print('no')

