from collections import deque

n,q = tuple([int(i) for i in input().split()])
lines = [input().split() for i in range(n)]
pro = deque([[i[0], int(i[1])] for i in lines])
time = 0

while True:
    left = pro.popleft()

    if left[1] - q > 0:
        time += q
        pro.append([left[0], left[1] - q])
    else:
        time += left[1]
        print(' '.join([left[0], str(time)]))

    if len(pro) == 0:
        break;