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
	L, R, d = rli()
	ans = 0
	for x in range(L, R+1):
		if x % d == 0:
			ans += 1
	print(ans)
	stdout.close()

if __name__ == "__main__":
	main()