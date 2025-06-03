N, X, T = map(int, input().split())

ans = 0
if N % X == 0:
	ans = N//X * T
else:
	ans = (N//X + 1) * T
	
print(ans)  