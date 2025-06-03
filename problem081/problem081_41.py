inputs = input().split(' ')
D = int(inputs[0])
T = int(inputs[1])
S = int(inputs[2])

t = D / S
if T >= t:
    print('Yes')
else:
    print('No')