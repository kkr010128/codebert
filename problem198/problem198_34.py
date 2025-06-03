n = map(int, raw_input().split(' '))[0]

def dfs(i, mx, n, cur = []):
	if i==n:
		print ''.join(cur)
		return
	for v in range(0, mx + 1): dfs(i + 1, mx + (1 if v == mx else 0), n , cur + [chr(v+ ord('a'))])

dfs(0,0,n)
