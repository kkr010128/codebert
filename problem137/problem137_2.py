n, *AB = map(int, open(0).read().split())
a = sorted(AB[::2])
b = sorted(AB[1::2])
if n % 2 == 0:
	print(b[n // 2 - 1] + b[n // 2] - a[n // 2 - 1] - a[n // 2] + 1)
else:
	print(b[(n + 1) // 2 - 1] - a[(n + 1) // 2 - 1] + 1)