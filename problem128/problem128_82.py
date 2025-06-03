def main():
	x, n = map(int, input().split())
	arr = set(list(map(int, input().split())))
	for d in range(0, 1000):
		for m in range(-1, 2, 2):
			y = x + m * d
			if y not in arr:
				print(y)
				return

main()