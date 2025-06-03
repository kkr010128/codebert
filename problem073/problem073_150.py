#from collections import deque
#from heapq import heapify, heappop, heappush
#from bisect import insort
#from math import gcd
#from decimal import Decimal
#mod = 1000000007
#mod = 998244353
#N = int(input())
#N, K = map(int, input().split())
#A = list(map(int, input().split()))
#flag = True
#for k in range(N):
#ans = 0
#print(ans)
#print('Yes')
#print('No')
N = int(input())
ans = 0

#N, K = map(int, input().split())
#A = list(map(int, input().split()))
#flag = True
for B in range(1, N+1):
	ans += N//B
	if N%B == 0:
		ans -= 1

#ans = 0
print(ans)
#print('Yes')
#print('No')