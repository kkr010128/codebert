import sys
n, m = map(int, input().split())
s = input()[::-1]
ans = []
tmp = 0
while tmp < n:
	for i in range(min(m, n-tmp), 0, -1):
		if s[tmp+i] == "0":
			tmp += i
			ans.append(str(i))
			break
	else:
		print(-1)
		sys.exit()
print(" ".join(ans[::-1]))