# ANSHUL GAUTAM
# IIIT-D

from math import *
from copy import *					# ll = deepcopy(l)
from heapq import *					# heappush(hp,x)
from string import *				# alpha = ascii_lowercase
from random import *				# l.sort(key=lambda l1:l1[0]-l1[1]) => ex: sort on the basis difference
from bisect import *				# bisect_left(arr,x,start,end)  => start and end parameters are temporary
from sys import stdin				# bisect_left return leftmost position where x should be inserted to keep sorted
from sys import maxsize				# minn = -maxsize
from operator import *				# d = sorted(d.items(), key=itemgetter(1))
from itertools import *				# pre = [0] + list(accumulate(l))
from decimal import Decimal 		# a = Decimal(a)	# use this for math questions
from collections import Counter		# d = dict(Counter(l))
from collections import defaultdict # d = defaultdict(list)

'''
5
24 11 8 3 16
'''

def solve(l):
	n = len(l)
	ans,maxx = 0,max(l)
	done = [0]*(maxx+1)
	l.sort()
	ans = 0
	d = dict(Counter(l))
	for i in l:
		zz = 2
		while(i*zz <= maxx):
			done[i*zz] = 1
			zz += 1
	for i in l:
		if(not done[i] and d[i] == 1):
			ans += 1
	return ans

N = int(stdin.readline())
l = list(map(int, stdin.readline().rstrip().split()))
ans = solve(l)
print(ans)

