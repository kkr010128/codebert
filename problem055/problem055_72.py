n = int(input())

oh = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for tr in range(n):
    b, f, r, v = map(int, input().split())
    oh[b - 1][f - 1][r - 1] += v
    
for k in range(4):
    for j in range(3):
        tmp = ''
        for i in range(10):
            tmp += (' ' + str(oh[k][j][i]))
        print(tmp)
    if k < 3:
        print('#' * 20)