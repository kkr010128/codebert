n = int(input())

s = 0
q = int(n ** .5)
for i in range(1, q+1):
	x = n // i
	s += i * (x * (x+1)) / 2
	if x**2 != n:
		y = max(n // (i+1), q)
		s += (i * (i+1) // 2) * ((x * (x+1) // 2) - (y * (y+1) // 2))

print(int(s))