# AtCoder
from collections import deque
S = input()
Q = int(input())
qs = [input().split() for i in range(Q)]

ans = deque(S)
flag = 0
count = 0
for q in qs:
    if q[0] == '1':
        if flag == 0:
            flag = 1
        else:
            flag = 0
        count += 1
    else:
        if flag == 0:
            if q[1] == '1':
                ans.appendleft(q[2])
            else:
                ans.append(q[2])
        else:
            if q[1] == '1':
                ans.append(q[2])
            else:
                ans.appendleft(q[2])

if count % 2 == 1:
    ans.reverse()

print(*ans, sep='')
