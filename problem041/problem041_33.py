a = input()
b = a.split(' ')
W = int(b[0])
H = int(b[1])
x = int(b[2])
y = int(b[3])
r = int(b[4])

if  -100 <= x < 0:
    print('No')
elif -100 <= y < 0:
    print('No')
elif W >= x + r and H >= y + r:
    print('Yes')
else:
    print('No')