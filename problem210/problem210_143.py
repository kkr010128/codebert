#ABC157E

n = int(input())
s = list(input())
q = int(input())
bits = [[0 for _ in range(n+1)] for _ in range(26)]
sl = []
for alp in s:
	alpord = ord(alp) - 97
	sl.append(alpord)
#print(bits) #test
#print(sl) #test
#print('クエリ開始') #test

def query(pos):
	ret = [0] * 26
	p = pos
	while p > 0:
		for i in range(26):
			ret[i] += bits[i][p]
		p -= p&(-p)
	return ret

def update(pos, a, x):
	r = pos
	while r <= n:
		bits[a][r] += x
		r += r&(-r)

for i in range(n):
	update(i+1, sl[i], 1)
#print(bits) #test

for _ in range(q):
	quer, xx, yy = map(str, input().split())
	if quer == '1':
		x = int(xx)
		y = ord(yy) - 97
		if sl[x-1] == y:
			continue
		else:
			update(x, sl[x-1], -1)
			update(x, y, 1)
			sl[x-1] = y
		#print('クエリ1でした') #test
		#print(bits) #test
		#print(sl) #test
	else:
		x = int(xx)
		y = int(yy)
		cnt1 = query(y)
		cnt2 = query(x-1)
		#print('クエリ2です') #test
		#print(cnt1) #test
		#print(cnt2) #test
		ans = 0
		for i in range(26):
			if cnt1[i] - cnt2[i] > 0:
				ans += 1
		print(ans)