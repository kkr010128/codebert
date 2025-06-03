k = int(input())
from collections import deque
q = deque() # FIFOキューの作成
for i in range(1,10):
    q.append(str(i))


for i in range(k-1):
    a = q.popleft()
    last = int(a[-1:])
    if last == 0:
        q.append(a+"0")
        q.append(a + "1")
    elif last ==9:
        q.append(a+"8")
        q.append(a + "9")
    else:
        q.append(a + str(last - 1))
        q.append(a + str(last ))
        q.append(a + str(last + 1))

print(q.popleft())