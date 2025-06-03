import math
a, b, c = map(int, input().split())
l = []; d = int(math.sqrt(c)); e = 0
for i in range(1, d + 1):
	if i * i == c: l += [i]
	elif c % i == 0: l += [i, c // i]
for x in l:
	if a <= x <= b: e += 1
print(e)