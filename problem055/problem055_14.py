n = int(input())
list = [[0 for i in range(10)] for j in range(12)]
for i in range(n):
    b,f,r,v = map(int,input().split())
    list[3*(b - 1)+(f - 1)][r - 1] += v
for i in range(12):
    if i % 3 == 0 and i != 0:
        print('####################')
    for j in range(10):
        print(' {}'.format(list[i][j]),end = "")
        if j == 9:
            print('')