x = int(input())
a = x // 100
b = x - a * 100

while b > 5:
	b = b - 5
	a -= 1

if a>=1:
	print(1)
else:
	print(0)