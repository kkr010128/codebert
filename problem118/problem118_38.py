# D - Sum of Divisors
N = int(input())
ans = (1 + N) * N

for i in range(2, N//2 + 1):
	j = 2
	
	while True:
		if i * j <= N:
			
			ans += i * j
			j += 1
		else:
			break

print(ans - 1)