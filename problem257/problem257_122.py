N = int(input())
A = list(map(int, input().split()))
ans = 0
now = 1
for i in range(N):
	if A[i] == now:
		now += 1
		continue
	else:
		ans += 1
if now == 1 and ans == N:
	print(-1)
else:
	print(ans)
