a = 100000;
n = int(input())
while n > 0:
	n -= 1
	a = 105*a//100
	a = ((a - 1) // 1000 + 1) * 1000
print(a)
