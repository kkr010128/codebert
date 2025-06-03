from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
import math

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def main():
	n = int(rl())
	ans = 0
	for i, a in enumerate(rli(), 1):
		if i % 2 == 1 and a % 2 == 1:
			ans += 1
	print(ans)
	stdout.close()

if __name__ == "__main__":
	main()