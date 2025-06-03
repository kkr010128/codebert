def main():
	N, M, X = [int(x) for x in input().split(" ")]
	# data[i] = List, data[i][0] = price, data[i][j(1:M)] = skill up of algorithm j
	data = [[int(a) for a in input().split(" ")] for i in range(N)]

	price = []
	for i in range(2 ** N):
		bit_book = list(zero_pad(format(i, 'b'), N))
		p = 0
		level = [0] * M
		for j in range(len(bit_book)):
			if bit_book[j] == "1":
				d = data[j]
				p += d[0]
				level = [l + b for (l, b) in zip(level, d[1:])]
		if min(level) >= X:
			price.append(p)
	if len(price) > 0:
		print(min(price))
	else:
		print(-1)

def zero_pad(s, n):
	s = str(s)
	return ("0" * n + s)[-n:]

main()