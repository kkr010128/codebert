def main():
	H, W, K = [int(k) for k in input().split(" ")]
	C = []
	black_in_row = []
	black_in_col = [0] * W
	for i in range(H):
		C.append(list(input()))
		black_in_row.append(C[i].count("#"))
		for j in range(W):
			if C[i][j] == "#":
				black_in_col[j] += 1

	black = sum(black_in_row)
	if black < K:
		print(0)
		return 0

	cnt = 0
	for i in range(2 ** H):
		row_bit = [f for f, b in enumerate(list(pad_zero(format(i, 'b'), H))) if b == "1"]
		r = sum([black_in_row[y] for y in row_bit])
		for j in range(2 ** W):
			col_bit = [f for f, b in enumerate(list(pad_zero(format(j, 'b'), W))) if b == "1"]
			c = sum([black_in_col[x] for x in col_bit])
			bl = black - r - c + sum([1 for p in row_bit for q in col_bit if C[p][q] == "#"])
			if bl == K:
				cnt += 1
	print(cnt)


def pad_zero(s, n):
	s = str(s)
	return ("0" * n + s)[-n:]

main()