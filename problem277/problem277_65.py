import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce


def input(): return sys.stdin.readline().strip()


def INT(): return int(input())


def MAP(): return map(int, input().split())


def LIST(): return list(map(int, input().split()))


def ZIP(n): return zip(*(MAP() for _ in range(n)))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


def main():
	H, W, K = MAP()
	cake = [list(input()) for _ in range(H)]
	cut = [[1 for _ in range(W)] for _ in range(H)]
	lis_0 = []
	lis_1 = []
	num = 1
	for i in range(H):
		if cake[i].count("#") > 0:
			lis_1.append(i)
		else:
			lis_0.append(i)
			continue

		ct = 0
		for j in range(W):
			if cake[i][j] == "#":
				ct += 1
				if ct < 2:
					cut[i][j] = num
				else:
					num += 1
					ct = 1
					cut[i][j] = num
			else:
				cut[i][j] = num

		num +=1

	# print(lis_0)
	# print(lis_1)

	for x in lis_0:
		ind = bisect(lis_1, x)
		# print(ind)
		if ind == len(lis_1):
			ind -= 1
		cut[x] = cut[lis_1[ind]]
		# print("x", cut[x])
		# print("ind", cut[lis_1[ind]])

	for x in cut:
		print(*x)


if __name__ == '__main__':
    main()
