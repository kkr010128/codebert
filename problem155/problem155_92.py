n , m = map(int,input().split())
h = list(map(int,input().split()))
ma = [0] * (n)
for i in range(m):
	a , b = map(int,input().split())
	a , b = a - 1 , b - 1
	ma[a] = max(ma[a] , h[b])
	ma[b] = max(ma[b] , h[a])

ans = 0
for i in range(n):
	ans += h[i] > ma[i]

print(ans)