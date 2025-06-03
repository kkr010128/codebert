import sys
n = int(input())
a = list(map(int,input().split()))
ans = 1

if 0 in a:
	print(0)
	sys.exit()

for i in range(n):
	ans = ans * a[i]
	if ans > 1000000000000000000:
		print(-1)
		sys.exit()

print(ans)