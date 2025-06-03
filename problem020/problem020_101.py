from collections import deque

n = int(input())
C = [input() for i in range(n)]

A = deque([])
for c in C:
	if c == 'deleteFirst':
		A.popleft()
	elif c == 'deleteLast':
		A.pop()
	elif 'delete' in c:
		q = int(c[7:])
		if q in A:
			A.remove(q)
	elif 'insert' in c:
		q = int(c[7:])
		A.appendleft(q)

print(' '.join(map(str, A)))
