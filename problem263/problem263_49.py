N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

count = 0

max = A[-1]
if max == 0:
	print(0)
	exit()

import math
V = [0]*(math.floor(math.log(max, 2))+1)

for i in range (0, N):
	B = A[i]
	vount = 0
	while B > 0:
		if B%2 == 0:
			B = B//2
			vount+=1			
		else:
			B = (B-1)//2
			V[vount]+=1
			vount+=1

for i in range (0, len(V)):
	count+=((V[i]*(N-V[i]))*(2**i))

print(count%(10**9+7))