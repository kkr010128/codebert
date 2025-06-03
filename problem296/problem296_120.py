s = input()
k = int(input())

ans = 0
lens = len(s)
# n -> n//2

def tansaku(moji, n, m, k):
	# n以上 m未満を探索する.
	ansr = 0
	cntt = 1
	for i in range(n, m-1):
		if moji[i] == moji[i + 1]:
			cntt += 1
		else:
			ansr += (cntt // 2) * k
			cntt = 1
	ansr += (cntt // 2) * k
	return ansr

cnnt = 1
hentai = False
for i in range(lens-1):
	if s[i] == s[i+1]:
		cnnt += 1
if cnnt == lens:
	hentai = True

if not hentai:
	if k >= 2:
		zencnts = 0
		atocnts = 0
		if s[lens-1] == s[0]:
			for i in range(lens):
				if s[lens-1-i] == s[lens-1]:
					zencnts += 1
				else:
					break
			for i in range(lens):
				if s[i] == s[0]:
					atocnts += 1
				else:
					break
		news = s[atocnts:] + s[:atocnts]
		news1 = s[atocnts:]
		news2 = s[:atocnts]
		ans += tansaku(news, 0, lens, k-1)
		ans += tansaku(news1, 0, lens-atocnts, 1)
		ans += tansaku(news2, 0, atocnts, 1)
		print(ans)
	else:
		ans += tansaku(s, 0, lens, 1)
		print(ans)
else:
	print((lens*k)//2)