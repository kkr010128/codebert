def sol(s, p):
	n = len(s)
	cnt = 0
	if p == 2 or p == 5:
		for i in range(n):
			if (s[i] % p == 0):
				cnt += i + 1
	else:
		pre = [0] * (n+2)
		pre[n+1] = 0
		b = 1
		for i in range(n, 0, -1):
			pre[i] = (pre[i+1] + s[i-1] * b) % p
			b = (b * 10) % p
		rec = [0] * p
		rec[0] = 1
		for i in range(n, 0, -1):
			cnt += rec[pre[i]]
			rec[pre[i]] += 1
	return cnt

if __name__ == "__main__":
	n, p = map(int, input().split())
	s = input()
	print (sol([int(i) for i in s], p))