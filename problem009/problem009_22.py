import sys
input = sys.stdin.readline
from collections import deque

def main():
	n = int(input().strip())
	v = [[] for _ in range(n)]
	for i in range(n):
		v[i] = list(map(int, input().strip().split()))
	l = [-1] * (n+1)
	q = deque()
	q.append((1, 0))
	while len(q) != 0:
		id, d = q.popleft()
		# print("id", id)
		if l[id] != -1:
			# print("b")
			continue
		l[id] = d
		# l[id] = min(d, l[id])
		# print(id, d)
		for i in range(v[id-1][1]):
			q.append((v[id-1][2+i], d+1))
			# if id == 8:
				# print("##", id, v[id-1][2+i])
				# print(repr(q))
	for i in range(1, n+1):
		print(i, l[i])

if __name__ == '__main__':
	main()

