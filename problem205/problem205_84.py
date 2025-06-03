from sys import stdin 
from collections import defaultdict, Counter


N, P = map(int, stdin.readline().split())
S, = stdin.readline().split()

ans = 0 


# 2 cases
if P == 2 or P == 5:
	digitdiv = []
	for i in range(N):
		if int(S[i]) % P == 0:
			ans += i + 1

else:
	#
	count = Counter()
	prefix = []
	ten = 1
	mod = 0
	for i in range(N):
		x = (int(S[N - i - 1])*ten + mod) % P 
		prefix.append(x)
		count[x] += 1
		ten = (ten * 10) % P 
		mod = x
	prefix.append(0)
	count[0] += 1
	for val in count.values():
		ans += val*(val - 1)//2


print (ans)



