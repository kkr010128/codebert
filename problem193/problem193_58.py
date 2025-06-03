def main():
	H, W, K = map(int, input().split())
	g = [input() for _ in range(H)]
	ans = 1 << 100
	for i in range(1 << H - 1):
		need = bin(i).count("1")
		sz = need + 1
		cnt = [0] * sz
		f = 1
		for j in range(W):
			c = 0
			for k in range(H):
				cnt[c] += g[k][j] == "1"
				if cnt[c] > K:
					break
				c += (i >> k) & 1
			else:
				continue
			cnt = [0] * sz
			need += 1
			if need > ans:
				f = 0
				break
			c = 0
			for k in range(H):
				cnt[c] += g[k][j] == "1"
				if cnt[c] > K:
					break
				c += (i >> k) & 1
			else:
				continue
			f = 0
			break
		if f:
			ans = min(ans, need)
	print(ans)

if __name__ == '__main__':
	main()