n,k = map(int,input().split())
w = []
for i in range(0,n):
	w.append(int(input()))

def check(p):
	i = 0
	for j in range(0,k):
		sm = 0
		while sm + w[i] <= p:
			sm = sm + w[i]
			i = i + 1
			if i == n:
				return n
	return i


def solve():
	r = 1000000000
	l = 0
	while r-l > 1:
		mid = int((r+l)/2)
		v = check(mid)
		if(v >= n):
			r = mid
		else:
			l = mid
	return r

print(solve())
