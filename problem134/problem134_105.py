n = input()
A = list(map(int, input().split()))

ans = 1
for a in A:
	ans *= a
	ans = min(ans, 10**18+1)

if ans == 10**18+1:
	ans = -1

print(ans)		