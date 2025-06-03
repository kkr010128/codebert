import math

while True:
	N = int(input())
	if N == 0:
		break
	
	S = list(map(int, input().split()))
	S2 = [x ** 2 for x in S]
	
	V = sum(S2)/N - (sum(S)/N) ** 2
	print(math.sqrt(V))