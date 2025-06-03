a = input()
b = a.split(' ')
c = int(b[0])
d = int(b[1])
if c < d:
    print('a < b')
elif c > d:
    print('a > b')
else:
    print('a == b')