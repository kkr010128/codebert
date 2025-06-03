import math

N = int(input())

Z = [int(input()) for i in range(N)]

ctr = 0

for j in range(N):
	if Z[j] == 2:
		ctr += 1
	elif Z[j] < 2 or (Z[j] % 2) == 0:
		pass
	else:
		Up = math.sqrt(Z[j])
		k = 3
		while k<= Up:
			if (Z[j] % k) == 0:
				break
			else:
				k += 1
		else:
			ctr += 1

print(ctr)