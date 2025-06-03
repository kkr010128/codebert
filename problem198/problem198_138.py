# パナソニック2020D
from queue import deque
n = int(input())
q = deque([("a", "a")])
while True:
    s, m = q.pop()
    if len(s)==n:
        print(s)
    elif len(s)>=n+1:
        break
    for o in range(ord("a"), ord(m)+2):
        if ord(m)<o:
            m = chr(o)
        q.appendleft((s + chr(o), m))