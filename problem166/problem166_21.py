import sys
from math import sqrt, gcd, ceil, log
from bisect import bisect
from collections import defaultdict
inp = sys.stdin.readline
read = lambda: list(map(int, inp().strip().split()))

# sys.setrecursionlimit(10**6)



def solve():
	s = inp().strip();
	dic = defaultdict(int); dic[0] = 1
	# sett.add(0)
	ans = 0; cum = 0
	for i in range(len(s)-1, -1, -1):
		cum += (int(s[i])*pow(10, (len(s)-i-1), 2019)) % 2019
		cum %= 2019
		dic[cum] += 1
	# print(dic)
	for i in dic:
		ans += ((dic[i])*(dic[i]-1))//2
	print(ans)






if __name__ == "__main__":
	solve()