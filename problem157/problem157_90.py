n = int(input())
a = list(map(int, input().split()))

l = {}
r = {}

for i, j in enumerate(a):
	if i - j in l:
		l[i-j] += 1
	else:
		l[i-j] = 1
	if i + j in r:
		r[i+j] += 1
	else:
		r[i+j] = 1
ans = 0
for i, j in l.items():
	if i in r:
		ans += r[i] * j

print(ans)