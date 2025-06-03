ans = [0 for _ in range(10001)]
for x in range(1, 101):
	for y in range(1, 101):
		for z in range(1, 101):
			w = x*x + y*y + z*z + x*y + y*z + z*x
			if w <= 10000:
				ans[w] += 1
print(*ans[1:int(input())+1], sep="\n")