
n = map(int, raw_input().split(' '))[0]


def dfs(i, mx, n, res, cur = []):
	if i==n:
		res.append(''.join(cur[::]))
		return


	for v in range(0, mx + 1):
		dfs(i + 1, mx + (1 if v == mx else 0), n , res, cur + [chr(v+ ord('a'))])

res =[]
dfs(0,0,n,res)
for w in res: print w