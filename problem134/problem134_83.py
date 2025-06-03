N = int(input())
A = map(int,input().split())
ans = 1
for x in A:
	ans *= x
	if ans > 10**18:
		ans = 10**18+1
print(-1 if ans > 10**18 else ans)