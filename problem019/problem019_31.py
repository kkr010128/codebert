# coding: utf-8
import sys
import collections

def main():
	n, quantum = map(int, raw_input().split())
	processes = [x.split() for x in sys.stdin.readlines()]
	for p in processes:
		p[1] = int(p[1])
	queue = collections.deque(processes)
	elapsed = 0
	while queue:
		# print elapsed, queue
		head = queue.popleft()
		if head[1] > quantum:
			head[1] -= quantum
			queue.append(head)
			elapsed += quantum
		else:
			elapsed += head[1]
			print head[0], elapsed

if __name__ == '__main__':
	main()