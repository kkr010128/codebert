n,q = [int(s) for s in input().split()]
queue = []
for i in range(n):
	name,time = input().split()
	queue.append([name,int(time)])

time = 0
while queue:
	processing = queue.pop(0)
	t = min(processing[1], q)
	time += t
	processing[1] -= t
	if processing[1] == 0:
		print(processing[0],time)
	else:
		queue.append(processing)