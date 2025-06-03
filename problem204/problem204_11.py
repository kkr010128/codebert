s = list(str(input()))
q = int(input())

from collections import deque
s = deque(s)

cnt = 0

for i in range(q):
    query = list(map(str, input().split()))
    if len(query) == 1:
        cnt += 1
    else:
        t, f, c = query
        if f == '1':
            if cnt%2 == 0:
                s.appendleft(c)
            else:
                s.append(c)
        else:
            if cnt%2 == 0:
                s.append(c)
            else:
                s.appendleft(c)
s = list(s)
if cnt%2 == 1:
    s.reverse()
print(''.join(s))
