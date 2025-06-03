n = int(input())
a = []
b = []
for i in range(n):
	a_1, b_1 = input().split()
	a.append(int(a_1))
	b.append(int(b_1))
a.sort()
b.sort()
is_odds = n % 2 == 0
if n % 2 == 0:
	print(b[n // 2 - 1] + b[n // 2] - a[n // 2 - 1] - a[n // 2] + 1)
else:
	print(b[(n + 1) // 2 - 1] - a[(n + 1) // 2 - 1] + 1)