N = int(input())

def calc(start, end):
	n = end // start
	return (n * (n+1) // 2) * start

ans = 0
for i in range(1, N+1):
	ans += calc(i, N//i * i)

print(ans)