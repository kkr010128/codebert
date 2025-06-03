inputs = input().split(' ')
inputs = list(map(int,inputs))

W = inputs[0]
H = inputs[1]
x = inputs[2]
y = inputs[3]
r = inputs[4]

if r <= x and x <= W-r and r <= y and y <= H-r :
    print('Yes')
else :
    print('No')