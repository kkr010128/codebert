def check(P):
	global k, T, n

	i = 0
	for j in range(k):
		s = 0
		while s + T[i] <= P:
			s += T[i]
			i += 1
			if (i == n):
				return n
	
	return i

def solve():
	left = 0
	right = 100000 * 10000

	while right - left > 1:
		mid = (left + right) // 2
		v = check(mid)
		if (v >= n):
			right = mid
		else:
			left = mid

	return right

if __name__ == '__main__':
	n, k = map(int, input().split())
	T = [int(input()) for i in range(n)]

	ans = solve()
	print(ans)