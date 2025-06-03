import sys
from collections import deque

n,q = map(int,input().split())
f = lambda n,t: (n,int(t))
queue = deque(f(*l.split()) for l in sys.stdin)

t = 0
while queue:
	name,time = queue.popleft()
	t += min(q, time)
	if time > q:
		queue.append((name, time-q))
	else:
		print(name,t)
