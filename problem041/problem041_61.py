i = input().split(' ')

W = int(i[0])
H = int(i[1])
x = int(i[2])
y = int(i[3])
r = int(i[4])

if x - r >= 0 and y - r >= 0 and x + r <= W and y + r <= H:
    print('Yes')
else:
   print('No')