from collections import deque

n = int(input())

q = deque()

for _ in range(n):
	com = input()
	if com[0] == "i":
		q.appendleft(com[7:])
	elif len(com) == 11:
		q.popleft()
	elif len(com) == 10:
		q.pop()
	else:
		try:
			q.remove(com[7:])
		except:
			pass


print(*q)

