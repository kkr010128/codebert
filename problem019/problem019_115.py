from collections import deque

def round_robin_scheduling(n, q, A):
	sum = 0

	while A:
		head = A.popleft()
		if head[1] <= q:
			sum += head[1]
			print(head[0], sum)
		else:
			sum += q
			head[1] -= q
			A.append(head)

if __name__ == '__main__':
	n, q = map(int, input().split())
	A = deque()

	for i in range(n):
		name, time = input().split()
		A.append([name, int(time)])
	
	round_robin_scheduling(n, q, A)