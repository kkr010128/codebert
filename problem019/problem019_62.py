n,q = map(int,input().split())
queue = []
for i in range(n):
	name,time = input().split()
	queue.append((name, int(time)))

t = 0
while queue:
	name,time = queue.pop(0)
	t += min(q, time)
	if time > q:
		queue.append((name, time-q))
	else:
		print(name,t)
