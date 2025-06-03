from collections import deque
q = deque()

for _ in range(int(input())):
	b=input()
	if b[0] == 'i':
		q.appendleft(b[7:])
	elif b[6] == ' ':
		try:
			q.remove(b[7:])
		except:
			pass
	elif len(b) > 10:
		q.popleft()
	elif len(b) > 6:
		q.pop()
print(*q)
