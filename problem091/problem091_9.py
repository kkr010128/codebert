import sys; input = sys.stdin.readline
n = int(input())
lis = list(map(int, input().split()))
ans = 0
for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			if lis[i] == lis[j] or lis[j] == lis[k] or lis[i] == lis[k]: continue
			s = sorted([lis[i], lis[j], lis[k]])
			if s[2] < s[1] + s[0]: ans += 1
print(ans)