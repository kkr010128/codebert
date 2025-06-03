x = tuple(input().split())
a = int(x[0])
b = int(x[1])
c = int(x[2])
k = 0
for n in range(1, c+1):
	if divmod(c, n)[1] == 0 and a <= divmod(c, n)[0] <= b:
		k += 1
print(k)