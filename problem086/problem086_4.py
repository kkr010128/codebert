from sys import stdin, stdout, setrecursionlimit
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from functools import lru_cache
import math

#setrecursionlimit(10**6)
rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())
rlf = lambda: map(float, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')
MOD = 10**9 + 7

def main():
	n, x, t = rli()
	q, r = divmod(n, x)
	ans = q*t 
	if r > 0:
		ans += t
	print(ans)
	stdout.close()

if __name__ == "__main__":
	main()