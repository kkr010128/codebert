n = int(input())
info = []
for _ in range(n):
    temp = [int(x) for x in input().split( )]
    info.append(temp)
state = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for a in info:
    state[a[0]-1][a[1]-1][a[2]-1] += a[3]
for b in range(4):
    for f in range(3):
        string = ''
        for k in range(10):
            string += ' ' + str(state[b][f][k])
        print(string)
    if b < 3:
        print('#'*20)

