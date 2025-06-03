n = int(input())
s = 0
for i in range(1, n+1):
	x = n // i
	s += i * (x * (x+1)) / 2 
print(int(s))