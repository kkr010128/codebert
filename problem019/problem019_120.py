from collections import deque

n, m = map(int, input().split())
name = ['']*n
time = ['']*n
for i in range(n):
	name[i], time[i] = input().split()
time = list(map(int, time))

Q = deque([i for i in range(n)])
t = 0
while Q!=deque([]):
	q = Q.popleft()
	if time[q]<=m:
		t += time[q]
		print(name[q] + ' ' + str(t))
	else:
		t += m
		time[q] -= m
		Q.append(q)
