stdin = [input() for i in range(3)]
line = stdin[0].split(' ')
A = int(line[0])
V = int(line[1])
line = stdin[1].split(' ')
B = int(line[0])
W = int(line[1])
T = int(stdin[2])
length = 0
if B > A:
    length = B-A
else:
    length = A-B
if (V-W)*T < length:
    print('NO')
else:
    print('YES')