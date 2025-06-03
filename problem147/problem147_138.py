a = [input() for i in range(2)]

s = a[0]
t = a[1]

if s == t[:-1]:
    print('Yes')
else:
    print('No')