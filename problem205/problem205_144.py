from sys import stdin 
from collections import Counter

N, P = map(int, stdin.readline().split())
S = stdin.readline().strip()

ans = 0
if P in (2, 5):
	for i in range(N):
		if int(S[i]) % P == 0:
			ans += i + 1


else:

	count = Counter()
	ten = 1
	mod = 0
	for i in range(N):
		x = (int(S[N - i - 1])*ten + mod) % P
		ten = ten*10 % P 
		mod = x
		count[x] += 1

	count[0] += 1


	for i in count.values():
		ans += i*(i - 1)//2

print (ans)