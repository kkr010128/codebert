(a, b, c) = map(lambda s:int(s), input().split())

r = 0
for n in range(a, b+1):
	if c % n == 0:
		r += 1

print(r)