import math
n = input()
A = 0

def is_prime(m):
	for i in range(2, int(math.sqrt(m)) + 1):
		if (m % i == 0):
			return False
	return True

for i in range(n):
	k = input()
	if is_prime(k):
		A += 1

print A