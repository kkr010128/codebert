n,q = map(int,raw_input().split())
task = []
lst = []
a = 0
for i in range(n):
    name,time = raw_input().split()
    task.append(int(time))
    lst.append(name)
while True:
	if task[0] > q:
		task[0] = task[0] - q
		task.append(task.pop(0))
		lst.append(lst.pop(0))
		a += q
	else:
		a += task[0]
		print lst[0],a
		task.pop(0)
		lst.pop(0)
		if len(lst) == 0:
			break