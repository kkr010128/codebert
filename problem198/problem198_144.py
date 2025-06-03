from collections import deque
import sys
n = int(input())
if n == 1:
    print('a')
    sys.exit()

q = deque([])
q.append((1, 'a', '1'))
cur = 1
while cur != n:
    num = len(q)
    j = 0
    while j < num:
        a, b, c = q.popleft()
        for i in range(1, max(map(int, list(c)))+2):
            q.append((i, b + chr(96+i), c + str(i)))
        j += 1
    cur += 1

for i in range(len(q)):
    a, b, c = q.popleft()
    print(b)

