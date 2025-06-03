natural = list(map(int, input().split()))
natural.sort
x = natural[1]
y = natural[0]
while (y != 0):
	x, y = y, x % y
print(x)