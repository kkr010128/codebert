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
	n = int(rl())
	x = pow(10, n, MOD) - 2*pow(9, n, MOD) + pow(8, n, MOD)
	print(x % MOD)
	stdout.close()

if __name__ == "__main__":
	main()