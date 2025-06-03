import sys
# from math import sqrt, gcd, ceil, log
# from bisect import bisect
from collections import defaultdict, Counter
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))

# sys.setrecursionlimit(10**6)



def solve():
	n = int(input()); arr = read()
	ans= 0
	for i in range(n):
		for j in range(i+1, n):
			ans += arr[i]*arr[j]
	print(ans)


		

if __name__ == "__main__":
	solve()
