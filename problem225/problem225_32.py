import math
H, A = list(map(int, input().split()))
if H % A == 0:
	print(H // A)
else:
	print(math.ceil(H / A))
